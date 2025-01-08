from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewTypeExternalAudio(BaseType):
    """
    The link is a link to an audio file
    """

    __type__: Literal["linkPreviewTypeExternalAudio"] = "linkPreviewTypeExternalAudio"

    url: str
    """URL of the audio file"""
    mime_type: str
    """MIME type of the audio file"""
    duration: int
    """Duration of the audio, in seconds; 0 if unknown"""
