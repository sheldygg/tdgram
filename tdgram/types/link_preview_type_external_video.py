from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewTypeExternalVideo(BaseType):
    """
    The link is a link to a video file
    """

    __type__: Literal["linkPreviewTypeExternalVideo"] = "linkPreviewTypeExternalVideo"

    url: str
    """URL of the video file"""
    mime_type: str
    """MIME type of the video file"""
    width: int
    """Expected width of the video preview; 0 if unknown"""
    height: int
    """Expected height of the video preview; 0 if unknown"""
    duration: int
    """Duration of the video, in seconds; 0 if unknown"""
