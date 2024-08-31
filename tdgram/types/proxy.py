from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ProxyType


@dataclass(kw_only=True)
class Proxy(BaseType):
    """
    Contains information about a proxy server
    """

    __type__: Literal["proxy"] = "proxy"

    id: int
    """Unique identifier of the proxy"""
    server: str
    """Proxy server domain or IP address"""
    port: int
    """Proxy server port"""
    last_used_date: int
    """Point in time (Unix timestamp) when the proxy was last used; 0 if never"""
    is_enabled: bool
    """True, if the proxy is enabled now"""
    type: ProxyType
    """Type of the proxy"""
