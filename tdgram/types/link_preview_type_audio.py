from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Audio


@dataclass(kw_only=True)
class LinkPreviewTypeAudio(BaseType):
    """
    The link is a link to an audio
    """

    __type__: Literal["linkPreviewTypeAudio"] = "linkPreviewTypeAudio"

    url: str | None = None
    """URL of the audio; may be empty if none"""
    mime_type: str
    """MIME type of the audio file"""
    audio: Audio | None = None
    """The audio description; may be null if unknown"""
    duration: int
    """Duration of the audio, in seconds; 0 if unknown"""
    author: str
    """Author of the audio"""
