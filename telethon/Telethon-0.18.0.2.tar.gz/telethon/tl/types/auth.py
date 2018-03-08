"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
import os
import struct


class Authorization(TLObject):
    CONSTRUCTOR_ID = 0xcd050916
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, user, tmp_sessions=None):
        """
        :param int | None tmp_sessions:
        :param User user:

        Constructor for auth.Authorization: Instance of Authorization.
        """
        super().__init__()

        self.tmp_sessions = tmp_sessions
        self.user = user

    def to_dict(self):
        return {
            '_': 'Authorization',
            'tmp_sessions': self.tmp_sessions,
            'user': None if self.user is None else self.user.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\x16\t\x05\xcd',
            struct.pack('<I', (0 if self.tmp_sessions is None or self.tmp_sessions is False else 1)),
            b'' if self.tmp_sessions is None or self.tmp_sessions is False else (struct.pack('<i', self.tmp_sessions)),
            bytes(self.user),
        ))

    @staticmethod
    def from_reader(reader):
        flags = reader.read_int()

        if flags & 1:
            _tmp_sessions = reader.read_int()
        else:
            _tmp_sessions = None
        _user = reader.tgread_object()
        return Authorization(user=_user, tmp_sessions=_tmp_sessions)


class CheckedPhone(TLObject):
    CONSTRUCTOR_ID = 0x811ea28e
    SUBCLASS_OF_ID = 0x99a3d765

    def __init__(self, phone_registered):
        """
        :param Bool phone_registered:

        Constructor for auth.CheckedPhone: Instance of CheckedPhone.
        """
        super().__init__()

        self.phone_registered = phone_registered

    def to_dict(self):
        return {
            '_': 'CheckedPhone',
            'phone_registered': self.phone_registered
        }

    def __bytes__(self):
        return b''.join((
            b'\x8e\xa2\x1e\x81',
            b'\xb5ur\x99' if self.phone_registered else b'7\x97y\xbc',
        ))

    @staticmethod
    def from_reader(reader):
        _phone_registered = reader.tgread_bool()
        return CheckedPhone(phone_registered=_phone_registered)


class CodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x741cd3e3
    SUBCLASS_OF_ID = 0xb3f3e401

    def __init__(self):
        super().__init__()

    def to_dict(self):
        return {
            '_': 'CodeTypeCall'
        }

    def __bytes__(self):
        return b''.join((
            b'\xe3\xd3\x1ct',
        ))

    @staticmethod
    def from_reader(reader):
        return CodeTypeCall()


class CodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0x226ccefb
    SUBCLASS_OF_ID = 0xb3f3e401

    def __init__(self):
        super().__init__()

    def to_dict(self):
        return {
            '_': 'CodeTypeFlashCall'
        }

    def __bytes__(self):
        return b''.join((
            b'\xfb\xcel"',
        ))

    @staticmethod
    def from_reader(reader):
        return CodeTypeFlashCall()


class CodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0x72a3158c
    SUBCLASS_OF_ID = 0xb3f3e401

    def __init__(self):
        super().__init__()

    def to_dict(self):
        return {
            '_': 'CodeTypeSms'
        }

    def __bytes__(self):
        return b''.join((
            b'\x8c\x15\xa3r',
        ))

    @staticmethod
    def from_reader(reader):
        return CodeTypeSms()


class ExportedAuthorization(TLObject):
    CONSTRUCTOR_ID = 0xdf969c2d
    SUBCLASS_OF_ID = 0x5fd1ec51

    def __init__(self, id, bytes):
        """
        :param int id:
        :param bytes bytes:

        Constructor for auth.ExportedAuthorization: Instance of ExportedAuthorization.
        """
        super().__init__()

        self.id = id
        self.bytes = bytes

    def to_dict(self):
        return {
            '_': 'ExportedAuthorization',
            'id': self.id,
            'bytes': self.bytes
        }

    def __bytes__(self):
        return b''.join((
            b'-\x9c\x96\xdf',
            struct.pack('<i', self.id),
            TLObject.serialize_bytes(self.bytes),
        ))

    @staticmethod
    def from_reader(reader):
        _id = reader.read_int()
        _bytes = reader.tgread_bytes()
        return ExportedAuthorization(id=_id, bytes=_bytes)


class PasswordRecovery(TLObject):
    CONSTRUCTOR_ID = 0x137948a5
    SUBCLASS_OF_ID = 0xfa72d43a

    def __init__(self, email_pattern):
        """
        :param str email_pattern:

        Constructor for auth.PasswordRecovery: Instance of PasswordRecovery.
        """
        super().__init__()

        self.email_pattern = email_pattern

    def to_dict(self):
        return {
            '_': 'PasswordRecovery',
            'email_pattern': self.email_pattern
        }

    def __bytes__(self):
        return b''.join((
            b'\xa5Hy\x13',
            TLObject.serialize_bytes(self.email_pattern),
        ))

    @staticmethod
    def from_reader(reader):
        _email_pattern = reader.tgread_string()
        return PasswordRecovery(email_pattern=_email_pattern)


class SentCode(TLObject):
    CONSTRUCTOR_ID = 0x5e002502
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, type, phone_code_hash, phone_registered=None, next_type=None, timeout=None):
        """
        :param bool | None phone_registered:
        :param auth.SentCodeType type:
        :param str phone_code_hash:
        :param auth.CodeType | None next_type:
        :param int | None timeout:

        Constructor for auth.SentCode: Instance of SentCode.
        """
        super().__init__()

        self.phone_registered = phone_registered
        self.type = type
        self.phone_code_hash = phone_code_hash
        self.next_type = next_type
        self.timeout = timeout

    def to_dict(self):
        return {
            '_': 'SentCode',
            'phone_registered': self.phone_registered,
            'type': None if self.type is None else self.type.to_dict(),
            'phone_code_hash': self.phone_code_hash,
            'next_type': None if self.next_type is None else self.next_type.to_dict(),
            'timeout': self.timeout
        }

    def __bytes__(self):
        return b''.join((
            b'\x02%\x00^',
            struct.pack('<I', (0 if self.phone_registered is None or self.phone_registered is False else 1) | (0 if self.next_type is None or self.next_type is False else 2) | (0 if self.timeout is None or self.timeout is False else 4)),
            bytes(self.type),
            TLObject.serialize_bytes(self.phone_code_hash),
            b'' if self.next_type is None or self.next_type is False else (bytes(self.next_type)),
            b'' if self.timeout is None or self.timeout is False else (struct.pack('<i', self.timeout)),
        ))

    @staticmethod
    def from_reader(reader):
        flags = reader.read_int()

        _phone_registered = bool(flags & 1)
        _type = reader.tgread_object()
        _phone_code_hash = reader.tgread_string()
        if flags & 2:
            _next_type = reader.tgread_object()
        else:
            _next_type = None
        if flags & 4:
            _timeout = reader.read_int()
        else:
            _timeout = None
        return SentCode(type=_type, phone_code_hash=_phone_code_hash, phone_registered=_phone_registered, next_type=_next_type, timeout=_timeout)


class SentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID = 0x3dbb5986
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length):
        """
        :param int length:

        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall.
        """
        super().__init__()

        self.length = length

    def to_dict(self):
        return {
            '_': 'SentCodeTypeApp',
            'length': self.length
        }

    def __bytes__(self):
        return b''.join((
            b'\x86Y\xbb=',
            struct.pack('<i', self.length),
        ))

    @staticmethod
    def from_reader(reader):
        _length = reader.read_int()
        return SentCodeTypeApp(length=_length)


class SentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID = 0x5353e5a7
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length):
        """
        :param int length:

        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall.
        """
        super().__init__()

        self.length = length

    def to_dict(self):
        return {
            '_': 'SentCodeTypeCall',
            'length': self.length
        }

    def __bytes__(self):
        return b''.join((
            b'\xa7\xe5SS',
            struct.pack('<i', self.length),
        ))

    @staticmethod
    def from_reader(reader):
        _length = reader.read_int()
        return SentCodeTypeCall(length=_length)


class SentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID = 0xab03c6d9
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, pattern):
        """
        :param str pattern:

        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall.
        """
        super().__init__()

        self.pattern = pattern

    def to_dict(self):
        return {
            '_': 'SentCodeTypeFlashCall',
            'pattern': self.pattern
        }

    def __bytes__(self):
        return b''.join((
            b'\xd9\xc6\x03\xab',
            TLObject.serialize_bytes(self.pattern),
        ))

    @staticmethod
    def from_reader(reader):
        _pattern = reader.tgread_string()
        return SentCodeTypeFlashCall(pattern=_pattern)


class SentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID = 0xc000bba2
    SUBCLASS_OF_ID = 0xff5b158e

    def __init__(self, length):
        """
        :param int length:

        Constructor for auth.SentCodeType: Instance of either SentCodeTypeApp, SentCodeTypeSms, SentCodeTypeCall, SentCodeTypeFlashCall.
        """
        super().__init__()

        self.length = length

    def to_dict(self):
        return {
            '_': 'SentCodeTypeSms',
            'length': self.length
        }

    def __bytes__(self):
        return b''.join((
            b'\xa2\xbb\x00\xc0',
            struct.pack('<i', self.length),
        ))

    @staticmethod
    def from_reader(reader):
        _length = reader.read_int()
        return SentCodeTypeSms(length=_length)
