from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetProxyLink(BaseMethod):
    """
    Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization
    """

    __type__: Literal["getProxyLink"] = "getProxyLink"
    __returning_type__ = HttpUrl

    proxy_id: int
    """Proxy identifier"""
