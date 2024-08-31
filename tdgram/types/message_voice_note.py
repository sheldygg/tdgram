from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, VoiceNote


@dataclass(kw_only=True)
class MessageVoiceNote(BaseType):
    """
    A voice note message
    """

    __type__: Literal["messageVoiceNote"] = "messageVoiceNote"

    voice_note: VoiceNote
    """The voice note description"""
    caption: FormattedText
    """Voice note caption"""
    is_listened: bool
    """True, if at least one of the recipients has listened to the voice note"""
