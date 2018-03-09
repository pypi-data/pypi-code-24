import typing
from datetime import datetime

DEFAULT_EXPIRE_TERM = 60 * 5  # second


class JwtInfo:
    def __init__(self, secret: str, algorithm: str, expire_term: int=DEFAULT_EXPIRE_TERM):
        self._secret = secret
        self._algorithm = algorithm
        self._expire_term = expire_term

    @property
    def secret(self) -> str:
        return self._secret

    @property
    def algorithm(self) -> str:
        return self._algorithm

    @property
    def expire_term(self) -> int:
        return self._expire_term


class AccessTokenInfo:
    def __init__(self, subject: str, u_idx: int, expire: int, client_id: str, scope: str):
        self._subject = subject
        self._u_idx = u_idx
        self._expire_timestamp = expire
        self._expire_date = datetime.fromtimestamp(expire)
        self._client_id = client_id
        self._scope = scope

    @property
    def subject(self) -> str:
        return self._subject

    @property
    def u_idx(self) -> int:
        return self._u_idx

    @property
    def expire_timestamp(self) -> int:
        return self._expire_timestamp

    @property
    def expire_date(self) -> datetime:
        return self._expire_date

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def scope(self) -> str:
        return self._scope

    @staticmethod
    def from_dict(dictionary: typing.Dict):
        return AccessTokenInfo(
            subject=dictionary['sub'], u_idx=dictionary['u_idx'], expire=dictionary['exp'], client_id=dictionary['client_id'],
            scope=dictionary['scope'],
        )
