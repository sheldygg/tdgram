from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import VoiceNote


@dataclass(kw_only=True)
class PushMessageContentVoiceNote(BaseType):
    """
    A voice note message
    """

    __type__: Literal["pushMessageContentVoiceNote"] = "pushMessageContentVoiceNote"

    voice_note: VoiceNote | None = None
    """Message content; may be null"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
