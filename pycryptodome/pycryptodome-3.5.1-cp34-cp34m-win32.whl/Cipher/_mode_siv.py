# ===================================================================
#
# Copyright (c) 2014, Legrandin <helderijs@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ===================================================================

"""
Synthetic Initialization Vector (SIV) mode.
"""

__all__ = ['SivMode']

from binascii import hexlify

from Crypto.Util.py3compat import byte_string, bord, unhexlify, b, bstr

from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Protocol.KDF import _S2V
from Crypto.Hash import BLAKE2s
from Crypto.Random import get_random_bytes


class SivMode(object):
    """Synthetic Initialization Vector (SIV).

    This is an Authenticated Encryption with Associated Data (`AEAD`_) mode.
    It provides both confidentiality and authenticity.

    The header of the message may be left in the clear, if needed, and it will
    still be subject to authentication. The decryption step tells the receiver
    if the message comes from a source that really knowns the secret key.
    Additionally, decryption detects if any part of the message - including the
    header - has been modified or corrupted.

    Unlike other AEAD modes such as CCM, EAX or GCM, accidental reuse of a
    nonce is not catastrophic for the confidentiality of the message. The only
    effect is that an attacker can tell when the same plaintext (and same
    associated data) is protected with the same key.

    The length of the MAC is fixed to the block size of the underlying cipher.
    The key size is twice the length of the key of the underlying cipher.

    This mode is only available for AES ciphers.

    +--------------------+---------------+-------------------+
    |      Cipher        | SIV MAC size  |   SIV key length  |
    |                    |    (bytes)    |     (bytes)       |
    +====================+===============+===================+
    |    AES-128         |      16       |        32         |
    +--------------------+---------------+-------------------+
    |    AES-192         |      16       |        48         |
    +--------------------+---------------+-------------------+
    |    AES-256         |      16       |        64         |
    +--------------------+---------------+-------------------+

    See `RFC5297`_ and the `original paper`__.

    .. _RFC5297: https://tools.ietf.org/html/rfc5297
    .. _AEAD: http://blog.cryptographyengineering.com/2012/05/how-to-choose-authenticated-encryption.html
    .. __: http://www.cs.ucdavis.edu/~rogaway/papers/keywrap.pdf

    :undocumented: __init__
    """

    def __init__(self, factory, key, nonce, kwargs):

        self.block_size = factory.block_size
        """The block size of the underlying cipher, in bytes."""

        self._factory = factory

        self._nonce = nonce
        self._cipher_params = kwargs

        if len(key) not in (32, 48, 64):
            raise ValueError("Incorrect key length (%d bytes)" % len(key))

        if nonce is not None:
            if isinstance(nonce, str):
                raise TypeError("When provided, the nonce must be a byte string")

            if len(nonce) == 0:
                raise ValueError("When provided, the nonce must be non-empty")

            self.nonce = bstr(nonce)
            """Public attribute is only available in case of non-deterministic
            encryption."""

        subkey_size = len(key) // 2

        self._mac_tag = None  # Cache for MAC tag
        self._kdf = _S2V(key[:subkey_size],
                         ciphermod=factory,
                         cipher_params=self._cipher_params)
        self._subkey_cipher = key[subkey_size:]

        # Purely for the purpose of verifying that cipher_params are OK
        factory.new(key[:subkey_size], factory.MODE_ECB, **kwargs)

        # Allowed transitions after initialization
        self._next = [self.update, self.encrypt, self.decrypt,
                      self.digest, self.verify]

    def _create_ctr_cipher(self, mac_tag):
        """Create a new CTR cipher from the MAC in SIV mode"""

        tag_int = bytes_to_long(bstr(mac_tag))
        return self._factory.new(
                    self._subkey_cipher,
                    self._factory.MODE_CTR,
                    initial_value=tag_int ^ (tag_int & 0x8000000080000000),
                    nonce=b(""),
                    **self._cipher_params)

    def update(self, component):
        """Protect one associated data component

        For SIV, the associated data is a sequence (*vector*) of non-empty
        byte strings (*components*).

        This method consumes the next component. It must be called
        once for each of the components that constitue the associated data.

        Note that the components have clear boundaries, so that:

            >>> cipher.update(b"builtin")
            >>> cipher.update(b"securely")

        is not equivalent to:

            >>> cipher.update(b"built")
            >>> cipher.update(b"insecurely")

        If there is no associated data, this method must not be called.

        :Parameters:
          component : byte string/array
            The next associated data component. It must not be empty.
        """

        if self.update not in self._next:
            raise TypeError("update() can only be called"
                                " immediately after initialization")

        self._next = [self.update, self.encrypt, self.decrypt,
                      self.digest, self.verify]

        return self._kdf.update(component)

    def encrypt(self, plaintext):
        """Encrypt data with the key and the parameters set at initialization.

        A cipher object is stateful: once you have encrypted a message
        you cannot encrypt (or decrypt) another message using the same
        object.

        This method can be called only **once**.

        You cannot reuse an object for encrypting
        or decrypting other data with the same key.

        This function does not add any padding to the plaintext.

        :Parameters:
          plaintext : byte string/array
            The piece of data to encrypt.
            It can be of any length, but it cannot be empty.
        :Return:
            the encrypted data, as a byte string.
            It is as long as *plaintext*.
        """

        if self.encrypt not in self._next:
            raise TypeError("encrypt() can only be called after"
                            " initialization or an update()")

        self._next = [self.digest]

        if self._nonce:
            self._kdf.update(self.nonce)
        self._kdf.update(plaintext)

        self._mac_tag = self._kdf.derive()
        cipher = self._create_ctr_cipher(self._mac_tag)

        return cipher.encrypt(plaintext)

    def decrypt(self, ciphertext):
        """Decrypt data with the key and the parameters set at initialization.

        For SIV, decryption and verification must take place at the same
        point. This method shall not be used.

        Use `decrypt_and_verify` instead.
        """

        raise TypeError("decrypt() not allowed for SIV mode."
                        " Use decrypt_and_verify() instead.")

    def digest(self):
        """Compute the *binary* MAC tag.

        The caller invokes this function at the very end.

        This method returns the MAC that shall be sent to the receiver,
        together with the ciphertext.

        :Return: the MAC, as a byte string.
        """

        if self.digest not in self._next:
            raise TypeError("digest() cannot be called when decrypting"
                            " or validating a message")
        self._next = [self.digest]
        if self._mac_tag is None:
            self._mac_tag = self._kdf.derive()
        return self._mac_tag

    def hexdigest(self):
        """Compute the *printable* MAC tag.

        This method is like `digest`.

        :Return: the MAC, as a hexadecimal string.
        """
        return "".join(["%02x" % bord(x) for x in self.digest()])

    def verify(self, received_mac_tag):
        """Validate the *binary* MAC tag.

        The caller invokes this function at the very end.

        This method checks if the decrypted message is indeed valid
        (that is, if the key is correct) and it has not been
        tampered with while in transit.

        :Parameters:
          received_mac_tag : byte string/array
            This is the *binary* MAC, as received from the sender.
        :Raises ValueError:
            if the MAC does not match. The message has been tampered with
            or the key is incorrect.
        """

        if self.verify not in self._next:
            raise TypeError("verify() cannot be called"
                            " when encrypting a message")
        self._next = [self.verify]

        if self._mac_tag is None:
            self._mac_tag = self._kdf.derive()

        secret = get_random_bytes(16)

        mac1 = BLAKE2s.new(digest_bits=160, key=secret, data=self._mac_tag)
        mac2 = BLAKE2s.new(digest_bits=160, key=secret, data=received_mac_tag)

        if mac1.digest() != mac2.digest():
            raise ValueError("MAC check failed")

    def hexverify(self, hex_mac_tag):
        """Validate the *printable* MAC tag.

        This method is like `verify`.

        :Parameters:
          hex_mac_tag : string
            This is the *printable* MAC, as received from the sender.
        :Raises ValueError:
            if the MAC does not match. The message has been tampered with
            or the key is incorrect.
        """

        self.verify(unhexlify(hex_mac_tag))

    def encrypt_and_digest(self, plaintext):
        """Perform encrypt() and digest() in one step.

        :Parameters:
          plaintext : byte string/array
            The piece of data to encrypt.
        :Return:
            a tuple with two byte strings:

            - the encrypted data
            - the MAC
        """

        return self.encrypt(plaintext), self.digest()

    def decrypt_and_verify(self, ciphertext, mac_tag):
        """Perform decryption and verification in one step.

        A cipher object is stateful: once you have decrypted a message
        you cannot decrypt (or encrypt) another message with the same
        object.

        You cannot reuse an object for encrypting
        or decrypting other data with the same key.

        This function does not remove any padding from the plaintext.

        :Parameters:
          ciphertext : byte string/array
            The piece of data to decrypt.
            It can be of any length.
          mac_tag : byte string/array
            This is the *binary* MAC, as received from the sender.

        :Return: the decrypted data (byte string).
        :Raises ValueError:
            if the MAC does not match. The message has been tampered with
            or the key is incorrect.
        """

        if self.decrypt not in self._next:
            raise TypeError("decrypt() can only be called"
                            " after initialization or an update()")
        self._next = [self.verify]

        # Take the MAC and start the cipher for decryption
        self._cipher = self._create_ctr_cipher(mac_tag)

        plaintext = self._cipher.decrypt(ciphertext)

        if self._nonce:
            self._kdf.update(self.nonce)
        if plaintext:
            self._kdf.update(plaintext)

        self.verify(mac_tag)
        return plaintext


def _create_siv_cipher(factory, **kwargs):
    """Create a new block cipher, configured in
    Synthetic Initializaton Vector (SIV) mode.

    :Parameters:

      factory : object
        A symmetric cipher module from `Crypto.Cipher`
        (like `Crypto.Cipher.AES`).

    :Keywords:

      key : byte string/array
        The secret key to use in the symmetric cipher.
        It must be 32, 48 or 64 bytes long.
        If AES is the chosen cipher, the variants *AES-128*,
        *AES-192* and or *AES-256* will be used internally.

      nonce : byte string/array
        For deterministic encryption, it is not present.

        Otherwise, it is a value that must never be reused
        for encrypting message under this key.

        There are no restrictions on its length,
        but it is recommended to use at least 16 bytes.
    """

    try:
        key = kwargs.pop("key")
    except KeyError as e:
        raise TypeError("Missing parameter: " + str(e))

    nonce = kwargs.pop("nonce", None)

    return SivMode(factory, key, nonce, kwargs)
