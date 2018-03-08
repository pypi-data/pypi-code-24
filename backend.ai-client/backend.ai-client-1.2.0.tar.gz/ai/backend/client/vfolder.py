from pathlib import Path
import re
from typing import Sequence, Union

import aiohttp

from .base import BaseFunction, SyncFunctionMixin
from .request import Request

__all__ = (
    'BaseVFolder',
    'VFolder',
)

_rx_slug = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?$')


class BaseVFolder(BaseFunction):
    @classmethod
    def _create(cls, name: str):
        assert _rx_slug.search(name) is not None
        resp = yield Request('POST', '/folders/', {
            'name': name,
        })
        return resp.json()

    @classmethod
    def _list(cls):
        resp = yield Request('GET', '/folders/')
        return resp.json()

    @classmethod
    def _get(cls, name: str):
        return cls(name)

    def _info(self):
        resp = yield Request('GET', '/folders/{0}'.format(self.name))
        return resp.json()

    def _delete(self):
        resp = yield Request('DELETE', '/folders/{0}'.format(self.name))
        if resp.status == 200:
            return resp.json()

    def _upload(self, files: Sequence[Union[str, Path]],
               basedir: Union[str, Path]=None):
        fields = []
        base_path = (Path.cwd() if basedir is None
                     else Path(basedir).resolve())
        for file in files:
            file_path = Path(file).resolve()
            try:
                fields.append(aiohttp.web.FileField(
                    'src',
                    str(file_path.relative_to(base_path)),
                    open(str(file_path), 'rb'),
                    'application/octet-stream',
                    None
                ))
            except ValueError:
                msg = 'File "{0}" is outside of the base directory "{1}".' \
                      .format(file_path, base_path)
                raise ValueError(msg) from None
        rqst = Request('POST', '/folders/{}/upload'.format(self.name))
        rqst.content = fields
        resp = yield rqst
        return resp

    def __init__(self, name: str):
        assert _rx_slug.search(name) is not None
        self.name = name
        self.delete = self._call_base_method(self._delete)
        self.info = self._call_base_method(self._info)
        self.upload = self._call_base_method(self._upload)

    def __init_subclass__(cls):
        cls.create = cls._call_base_clsmethod(cls._create)
        cls.list = cls._call_base_clsmethod(cls._list)
        cls.get = cls._call_base_clsmethod(cls._get)


class VFolder(SyncFunctionMixin, BaseVFolder):
    pass
