from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ProxyTypeSocks5(BaseType):
    """
    A SOCKS5 proxy server
    """

    __type__: Literal["proxyTypeSocks5"] = "proxyTypeSocks5"

    username: str | None = None
    """Username for logging in; may be empty"""
    password: str | None = None
    """Password for logging in; may be empty"""
