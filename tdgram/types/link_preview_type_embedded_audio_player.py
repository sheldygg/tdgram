from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class LinkPreviewTypeEmbeddedAudioPlayer(BaseType):
    """
    The link is a link to an audio player
    """

    __type__: Literal["linkPreviewTypeEmbeddedAudioPlayer"] = "linkPreviewTypeEmbeddedAudioPlayer"

    url: str
    """URL of the external audio player"""
    thumbnail: Photo | None = None
    """Thumbnail of the audio; may be null if unknown"""
    duration: int
    """Duration of the audio, in seconds"""
    author: str
    """Author of the audio"""
    width: int
    """Expected width of the embedded player"""
    height: int
    """Expected height of the embedded player"""
