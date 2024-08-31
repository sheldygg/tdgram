from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Proxy, ProxyType
from .base import BaseMethod


@dataclass(kw_only=True)
class EditProxy(BaseMethod):
    """
    Edits an existing proxy server for network requests. Can be called before authorization
    """

    __type__: Literal["editProxy"] = "editProxy"
    __returning_type__ = Proxy

    proxy_id: int
    """Proxy identifier"""
    server: str
    """Proxy server domain or IP address"""
    port: int
    """Proxy server port"""
    enable: bool
    """Pass true to immediately enable the proxy"""
    type: ProxyType
    """Proxy type"""
