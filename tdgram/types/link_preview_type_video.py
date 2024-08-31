from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Video


@dataclass(kw_only=True)
class LinkPreviewTypeVideo(BaseType):
    """
    The link is a link to a video
    """

    __type__: Literal["linkPreviewTypeVideo"] = "linkPreviewTypeVideo"

    url: str | None = None
    """URL of the video; may be empty if none"""
    mime_type: str
    """MIME type of the video file"""
    video: Video | None = None
    """The video description; may be null if unknown"""
    width: int
    """Expected width of the preview"""
    height: int
    """Expected height of the preview"""
    duration: int
    """Duration of the video, in seconds; 0 if unknown"""
    author: str
    """Author of the video"""
