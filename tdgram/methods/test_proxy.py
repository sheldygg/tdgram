from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ProxyType
from .base import BaseMethod


@dataclass(kw_only=True)
class TestProxy(BaseMethod):
    """
    Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization
    """

    __type__: Literal["testProxy"] = "testProxy"
    __returning_type__ = Ok

    server: str
    """Proxy server domain or IP address"""
    port: int
    """Proxy server port"""
    type: ProxyType
    """Proxy type"""
    dc_id: int
    """Identifier of a datacenter with which to test connection"""
    timeout: float
    """The maximum overall timeout for the request"""
