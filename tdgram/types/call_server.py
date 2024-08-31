from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CallServerType


@dataclass(kw_only=True)
class CallServer(BaseType):
    """
    Describes a server for relaying call data
    """

    __type__: Literal["callServer"] = "callServer"

    id: int
    """Server identifier"""
    ip_address: str
    """Server IPv4 address"""
    ipv6_address: str
    """Server IPv6 address"""
    port: int
    """Server port number"""
    type: CallServerType
    """Server type"""
