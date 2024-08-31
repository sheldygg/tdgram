from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallServerTypeWebrtc(BaseType):
    """
    A WebRTC server
    """

    __type__: Literal["callServerTypeWebrtc"] = "callServerTypeWebrtc"

    username: str
    """Username to be used for authentication"""
    password: str
    """Authentication password"""
    supports_turn: bool
    """True, if the server supports TURN"""
    supports_stun: bool
    """True, if the server supports STUN"""
