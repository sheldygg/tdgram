from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DiscardCall(BaseMethod):
    """
    Discards a call
    """

    __type__: Literal["discardCall"] = "discardCall"
    __returning_type__ = Ok

    call_id: int
    """Call identifier"""
    is_disconnected: bool
    """Pass true if the user was disconnected"""
    duration: int
    """The call duration, in seconds"""
    is_video: bool
    """Pass true if the call was a video call"""
    connection_id: int
    """Identifier of the connection used during the call"""
