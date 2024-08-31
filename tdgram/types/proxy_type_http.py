from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ProxyTypeHttp(BaseType):
    """
    A HTTP transparent proxy server
    """

    __type__: Literal["proxyTypeHttp"] = "proxyTypeHttp"

    username: str | None = None
    """Username for logging in; may be empty"""
    password: str | None = None
    """Password for logging in; may be empty"""
    http_only: bool
    """Pass true if the proxy supports only HTTP requests and doesn't support transparent TCP connections via HTTP CONNECT method"""
