from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PageBlockCaption, VoiceNote


@dataclass(kw_only=True)
class PageBlockVoiceNote(BaseType):
    """
    A voice note
    """

    __type__: Literal["pageBlockVoiceNote"] = "pageBlockVoiceNote"

    voice_note: VoiceNote | None = None
    """Voice note; may be null"""
    caption: PageBlockCaption
    """Voice note caption"""
