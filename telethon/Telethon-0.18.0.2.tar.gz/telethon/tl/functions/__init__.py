"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from . import contest, auth, account, users, contacts, messages, updates, photos, upload, help, channels, bots, payments, stickers, phone, langpack
import os
import struct


class DestroyAuthKeyRequest(TLObject):
    CONSTRUCTOR_ID = 0xd1435160
    SUBCLASS_OF_ID = 0x8291e68e

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'DestroyAuthKeyRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'`QC\xd1',
        ))

    @staticmethod
    def from_reader(reader):
        return DestroyAuthKeyRequest()


class DestroySessionRequest(TLObject):
    CONSTRUCTOR_ID = 0xe7512126
    SUBCLASS_OF_ID = 0xaf0ce7bd

    def __init__(self, session_id):
        """
        :param int session_id:

        :returns DestroySessionRes: Instance of either DestroySessionOk, DestroySessionNone.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.session_id = session_id

    def to_dict(self):
        return {
            '_': 'DestroySessionRequest',
            'session_id': self.session_id
        }

    def __bytes__(self):
        return b''.join((
            b'&!Q\xe7',
            struct.pack('<q', self.session_id),
        ))

    @staticmethod
    def from_reader(reader):
        _session_id = reader.read_long()
        return DestroySessionRequest(session_id=_session_id)


class GetFutureSaltsRequest(TLObject):
    CONSTRUCTOR_ID = 0xb921bd04
    SUBCLASS_OF_ID = 0x1090f517

    def __init__(self, num):
        """
        :param int num:

        :returns FutureSalts: Instance of FutureSalts.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.num = num

    def to_dict(self):
        return {
            '_': 'GetFutureSaltsRequest',
            'num': self.num
        }

    def __bytes__(self):
        return b''.join((
            b'\x04\xbd!\xb9',
            struct.pack('<i', self.num),
        ))

    @staticmethod
    def from_reader(reader):
        _num = reader.read_int()
        return GetFutureSaltsRequest(num=_num)


class InitConnectionRequest(TLObject):
    CONSTRUCTOR_ID = 0xc7481da6
    SUBCLASS_OF_ID = 0xb7b2364b

    def __init__(self, api_id, device_model, system_version, app_version, system_lang_code, lang_pack, lang_code, query):
        """
        :param int api_id:
        :param str device_model:
        :param str system_version:
        :param str app_version:
        :param str system_lang_code:
        :param str lang_pack:
        :param str lang_code:
        :param X query:

        :returns X: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.api_id = api_id
        self.device_model = device_model
        self.system_version = system_version
        self.app_version = app_version
        self.system_lang_code = system_lang_code
        self.lang_pack = lang_pack
        self.lang_code = lang_code
        self.query = query

    def to_dict(self):
        return {
            '_': 'InitConnectionRequest',
            'api_id': self.api_id,
            'device_model': self.device_model,
            'system_version': self.system_version,
            'app_version': self.app_version,
            'system_lang_code': self.system_lang_code,
            'lang_pack': self.lang_pack,
            'lang_code': self.lang_code,
            'query': None if self.query is None else self.query.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\xa6\x1dH\xc7',
            struct.pack('<i', self.api_id),
            TLObject.serialize_bytes(self.device_model),
            TLObject.serialize_bytes(self.system_version),
            TLObject.serialize_bytes(self.app_version),
            TLObject.serialize_bytes(self.system_lang_code),
            TLObject.serialize_bytes(self.lang_pack),
            TLObject.serialize_bytes(self.lang_code),
            bytes(self.query),
        ))

    @staticmethod
    def from_reader(reader):
        _api_id = reader.read_int()
        _device_model = reader.tgread_string()
        _system_version = reader.tgread_string()
        _app_version = reader.tgread_string()
        _system_lang_code = reader.tgread_string()
        _lang_pack = reader.tgread_string()
        _lang_code = reader.tgread_string()
        _query = reader.tgread_object()
        return InitConnectionRequest(api_id=_api_id, device_model=_device_model, system_version=_system_version, app_version=_app_version, system_lang_code=_system_lang_code, lang_pack=_lang_pack, lang_code=_lang_code, query=_query)


class InvokeAfterMsgRequest(TLObject):
    CONSTRUCTOR_ID = 0xcb9f372d
    SUBCLASS_OF_ID = 0xb7b2364b

    def __init__(self, msg_id, query):
        """
        :param int msg_id:
        :param X query:

        :returns X: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.msg_id = msg_id
        self.query = query

    def to_dict(self):
        return {
            '_': 'InvokeAfterMsgRequest',
            'msg_id': self.msg_id,
            'query': None if self.query is None else self.query.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'-7\x9f\xcb',
            struct.pack('<q', self.msg_id),
            bytes(self.query),
        ))

    @staticmethod
    def from_reader(reader):
        _msg_id = reader.read_long()
        _query = reader.tgread_object()
        return InvokeAfterMsgRequest(msg_id=_msg_id, query=_query)


class InvokeAfterMsgsRequest(TLObject):
    CONSTRUCTOR_ID = 0x3dc4b4f0
    SUBCLASS_OF_ID = 0xb7b2364b

    def __init__(self, msg_ids, query):
        """
        :param list[int] msg_ids:
        :param X query:

        :returns X: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.msg_ids = msg_ids
        self.query = query

    def to_dict(self):
        return {
            '_': 'InvokeAfterMsgsRequest',
            'msg_ids': [] if self.msg_ids is None else self.msg_ids[:],
            'query': None if self.query is None else self.query.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\xf0\xb4\xc4=',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.msg_ids)),b''.join(struct.pack('<q', x) for x in self.msg_ids),
            bytes(self.query),
        ))

    @staticmethod
    def from_reader(reader):
        reader.read_int()
        _msg_ids = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _msg_ids.append(_x)

        _query = reader.tgread_object()
        return InvokeAfterMsgsRequest(msg_ids=_msg_ids, query=_query)


class InvokeWithLayerRequest(TLObject):
    CONSTRUCTOR_ID = 0xda9b0d0d
    SUBCLASS_OF_ID = 0xb7b2364b

    def __init__(self, layer, query):
        """
        :param int layer:
        :param X query:

        :returns X: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.layer = layer
        self.query = query

    def to_dict(self):
        return {
            '_': 'InvokeWithLayerRequest',
            'layer': self.layer,
            'query': None if self.query is None else self.query.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\r\r\x9b\xda',
            struct.pack('<i', self.layer),
            bytes(self.query),
        ))

    @staticmethod
    def from_reader(reader):
        _layer = reader.read_int()
        _query = reader.tgread_object()
        return InvokeWithLayerRequest(layer=_layer, query=_query)


class InvokeWithoutUpdatesRequest(TLObject):
    CONSTRUCTOR_ID = 0xbf9459b7
    SUBCLASS_OF_ID = 0xb7b2364b

    def __init__(self, query):
        """
        :param X query:

        :returns X: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.query = query

    def to_dict(self):
        return {
            '_': 'InvokeWithoutUpdatesRequest',
            'query': None if self.query is None else self.query.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\xb7Y\x94\xbf',
            bytes(self.query),
        ))

    @staticmethod
    def from_reader(reader):
        _query = reader.tgread_object()
        return InvokeWithoutUpdatesRequest(query=_query)


class PingRequest(TLObject):
    CONSTRUCTOR_ID = 0x7abe77ec
    SUBCLASS_OF_ID = 0x816aee71

    def __init__(self, ping_id):
        """
        :param int ping_id:

        :returns Pong: Instance of Pong.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.ping_id = ping_id

    def to_dict(self):
        return {
            '_': 'PingRequest',
            'ping_id': self.ping_id
        }

    def __bytes__(self):
        return b''.join((
            b'\xecw\xbez',
            struct.pack('<q', self.ping_id),
        ))

    @staticmethod
    def from_reader(reader):
        _ping_id = reader.read_long()
        return PingRequest(ping_id=_ping_id)


class PingDelayDisconnectRequest(TLObject):
    CONSTRUCTOR_ID = 0xf3427b8c
    SUBCLASS_OF_ID = 0x816aee71

    def __init__(self, ping_id, disconnect_delay):
        """
        :param int ping_id:
        :param int disconnect_delay:

        :returns Pong: Instance of Pong.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.ping_id = ping_id
        self.disconnect_delay = disconnect_delay

    def to_dict(self):
        return {
            '_': 'PingDelayDisconnectRequest',
            'ping_id': self.ping_id,
            'disconnect_delay': self.disconnect_delay
        }

    def __bytes__(self):
        return b''.join((
            b'\x8c{B\xf3',
            struct.pack('<q', self.ping_id),
            struct.pack('<i', self.disconnect_delay),
        ))

    @staticmethod
    def from_reader(reader):
        _ping_id = reader.read_long()
        _disconnect_delay = reader.read_int()
        return PingDelayDisconnectRequest(ping_id=_ping_id, disconnect_delay=_disconnect_delay)


class ReqDHParamsRequest(TLObject):
    CONSTRUCTOR_ID = 0xd712e4be
    SUBCLASS_OF_ID = 0xa6188d9e

    def __init__(self, nonce, server_nonce, p, q, public_key_fingerprint, encrypted_data):
        """
        :param int nonce:
        :param int server_nonce:
        :param bytes p:
        :param bytes q:
        :param int public_key_fingerprint:
        :param bytes encrypted_data:

        :returns Server_DH_Params: Instance of either ServerDHParamsFail, ServerDHParamsOk.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.nonce = nonce
        self.server_nonce = server_nonce
        self.p = p
        self.q = q
        self.public_key_fingerprint = public_key_fingerprint
        self.encrypted_data = encrypted_data

    def to_dict(self):
        return {
            '_': 'ReqDHParamsRequest',
            'nonce': self.nonce,
            'server_nonce': self.server_nonce,
            'p': self.p,
            'q': self.q,
            'public_key_fingerprint': self.public_key_fingerprint,
            'encrypted_data': self.encrypted_data
        }

    def __bytes__(self):
        return b''.join((
            b'\xbe\xe4\x12\xd7',
            self.nonce.to_bytes(16, 'little', signed=True),
            self.server_nonce.to_bytes(16, 'little', signed=True),
            TLObject.serialize_bytes(self.p),
            TLObject.serialize_bytes(self.q),
            struct.pack('<q', self.public_key_fingerprint),
            TLObject.serialize_bytes(self.encrypted_data),
        ))

    @staticmethod
    def from_reader(reader):
        _nonce = reader.read_large_int(bits=128)
        _server_nonce = reader.read_large_int(bits=128)
        _p = reader.tgread_bytes()
        _q = reader.tgread_bytes()
        _public_key_fingerprint = reader.read_long()
        _encrypted_data = reader.tgread_bytes()
        return ReqDHParamsRequest(nonce=_nonce, server_nonce=_server_nonce, p=_p, q=_q, public_key_fingerprint=_public_key_fingerprint, encrypted_data=_encrypted_data)


class ReqPqRequest(TLObject):
    CONSTRUCTOR_ID = 0x60469778
    SUBCLASS_OF_ID = 0x786986b8

    def __init__(self, nonce):
        """
        :param int nonce:

        :returns ResPQ: Instance of ResPQ.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.nonce = nonce

    def to_dict(self):
        return {
            '_': 'ReqPqRequest',
            'nonce': self.nonce
        }

    def __bytes__(self):
        return b''.join((
            b'x\x97F`',
            self.nonce.to_bytes(16, 'little', signed=True),
        ))

    @staticmethod
    def from_reader(reader):
        _nonce = reader.read_large_int(bits=128)
        return ReqPqRequest(nonce=_nonce)


class ReqPqMultiRequest(TLObject):
    CONSTRUCTOR_ID = 0xbe7e8ef1
    SUBCLASS_OF_ID = 0x786986b8

    def __init__(self, nonce):
        """
        :param int nonce:

        :returns ResPQ: Instance of ResPQ.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.nonce = nonce

    def to_dict(self):
        return {
            '_': 'ReqPqMultiRequest',
            'nonce': self.nonce
        }

    def __bytes__(self):
        return b''.join((
            b'\xf1\x8e~\xbe',
            self.nonce.to_bytes(16, 'little', signed=True),
        ))

    @staticmethod
    def from_reader(reader):
        _nonce = reader.read_large_int(bits=128)
        return ReqPqMultiRequest(nonce=_nonce)


class RpcDropAnswerRequest(TLObject):
    CONSTRUCTOR_ID = 0x58e4a740
    SUBCLASS_OF_ID = 0x4bca7570

    def __init__(self, req_msg_id):
        """
        :param int req_msg_id:

        :returns RpcDropAnswer: Instance of either RpcAnswerUnknown, RpcAnswerDroppedRunning, RpcAnswerDropped.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.req_msg_id = req_msg_id

    def to_dict(self):
        return {
            '_': 'RpcDropAnswerRequest',
            'req_msg_id': self.req_msg_id
        }

    def __bytes__(self):
        return b''.join((
            b'@\xa7\xe4X',
            struct.pack('<q', self.req_msg_id),
        ))

    @staticmethod
    def from_reader(reader):
        _req_msg_id = reader.read_long()
        return RpcDropAnswerRequest(req_msg_id=_req_msg_id)


class SetClientDHParamsRequest(TLObject):
    CONSTRUCTOR_ID = 0xf5045f1f
    SUBCLASS_OF_ID = 0x55dd6cdb

    def __init__(self, nonce, server_nonce, encrypted_data):
        """
        :param int nonce:
        :param int server_nonce:
        :param bytes encrypted_data:

        :returns Set_client_DH_params_answer: Instance of either DhGenOk, DhGenRetry, DhGenFail.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_data = encrypted_data

    def to_dict(self):
        return {
            '_': 'SetClientDHParamsRequest',
            'nonce': self.nonce,
            'server_nonce': self.server_nonce,
            'encrypted_data': self.encrypted_data
        }

    def __bytes__(self):
        return b''.join((
            b'\x1f_\x04\xf5',
            self.nonce.to_bytes(16, 'little', signed=True),
            self.server_nonce.to_bytes(16, 'little', signed=True),
            TLObject.serialize_bytes(self.encrypted_data),
        ))

    @staticmethod
    def from_reader(reader):
        _nonce = reader.read_large_int(bits=128)
        _server_nonce = reader.read_large_int(bits=128)
        _encrypted_data = reader.tgread_bytes()
        return SetClientDHParamsRequest(nonce=_nonce, server_nonce=_server_nonce, encrypted_data=_encrypted_data)
