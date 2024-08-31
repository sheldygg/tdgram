from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ProxyType


@dataclass(kw_only=True)
class InternalLinkTypeProxy(BaseType):
    """
    The link is a link to a proxy. Call addProxy with the given parameters to process the link and add the proxy
    """

    __type__: Literal["internalLinkTypeProxy"] = "internalLinkTypeProxy"

    server: str
    """Proxy server domain or IP address"""
    port: int
    """Proxy server port"""
    type: ProxyType
    """Type of the proxy"""
