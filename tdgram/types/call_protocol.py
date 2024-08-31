from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallProtocol(BaseType):
    """
    Specifies the supported call protocols
    """

    __type__: Literal["callProtocol"] = "callProtocol"

    udp_p2p: bool
    """True, if UDP peer-to-peer connections are supported"""
    udp_reflector: bool
    """True, if connection through UDP reflectors is supported"""
    min_layer: int
    """The minimum supported API layer; use 65"""
    max_layer: int
    """The maximum supported API layer; use 92"""
    library_versions: list[str]
    """List of supported tgcalls versions"""
