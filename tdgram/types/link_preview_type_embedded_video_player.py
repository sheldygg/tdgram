from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class LinkPreviewTypeEmbeddedVideoPlayer(BaseType):
    """
    The link is a link to a video player
    """

    __type__: Literal["linkPreviewTypeEmbeddedVideoPlayer"] = "linkPreviewTypeEmbeddedVideoPlayer"

    url: str
    """URL of the external video player"""
    thumbnail: Photo | None = None
    """Thumbnail of the video; may be null if unknown"""
    duration: int
    """Duration of the video, in seconds"""
    author: str
    """Author of the video"""
    width: int
    """Expected width of the embedded player"""
    height: int
    """Expected height of the embedded player"""
