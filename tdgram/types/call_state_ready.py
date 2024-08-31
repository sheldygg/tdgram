from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CallProtocol, CallServer


@dataclass(kw_only=True)
class CallStateReady(BaseType):
    """
    The call is ready to use
    """

    __type__: Literal["callStateReady"] = "callStateReady"

    protocol: CallProtocol
    """Call protocols supported by the other call participant"""
    servers: list[CallServer]
    """List of available call servers"""
    config: str
    """A JSON-encoded call config"""
    encryption_key: bytes
    """Call encryption key"""
    emojis: list[str]
    """Encryption key fingerprint represented as 4 emoji"""
    allow_p2p: bool
    """True, if peer-to-peer connection is allowed by users privacy settings"""
    custom_parameters: str
    """Custom JSON-encoded call parameters to be passed to tgcalls"""
