from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CallDiscardReason


@dataclass(kw_only=True)
class MessageCall(BaseType):
    """
    A message with information about an ended call
    """

    __type__: Literal["messageCall"] = "messageCall"

    is_video: bool
    """True, if the call was a video call"""
    discard_reason: CallDiscardReason
    """Reason why the call was discarded"""
    duration: int
    """Call duration, in seconds"""
