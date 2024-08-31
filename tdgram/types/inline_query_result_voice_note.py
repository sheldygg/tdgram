from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import VoiceNote


@dataclass(kw_only=True)
class InlineQueryResultVoiceNote(BaseType):
    """
    Represents a voice note
    """

    __type__: Literal["inlineQueryResultVoiceNote"] = "inlineQueryResultVoiceNote"

    id: str
    """Unique identifier of the query result"""
    voice_note: VoiceNote
    """Voice note"""
    title: str
    """Title of the voice note"""
