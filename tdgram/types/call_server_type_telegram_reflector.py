from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallServerTypeTelegramReflector(BaseType):
    """
    A Telegram call reflector
    """

    __type__: Literal["callServerTypeTelegramReflector"] = "callServerTypeTelegramReflector"

    peer_tag: bytes
    """A peer tag to be used with the reflector"""
    is_tcp: bool
    """True, if the server uses TCP instead of UDP"""
