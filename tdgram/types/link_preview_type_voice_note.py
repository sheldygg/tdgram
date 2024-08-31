from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import VoiceNote


@dataclass(kw_only=True)
class LinkPreviewTypeVoiceNote(BaseType):
    """
    The link is a link to a voice note message
    """

    __type__: Literal["linkPreviewTypeVoiceNote"] = "linkPreviewTypeVoiceNote"

    voice_note: VoiceNote
    """The voice note"""
