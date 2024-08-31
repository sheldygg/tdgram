from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Audio


@dataclass(kw_only=True)
class PushMessageContentAudio(BaseType):
    """
    An audio message
    """

    __type__: Literal["pushMessageContentAudio"] = "pushMessageContentAudio"

    audio: Audio | None = None
    """Message content; may be null"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
