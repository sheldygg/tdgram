from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentMediaAlbum(BaseType):
    """
    A media album
    """

    __type__: Literal["pushMessageContentMediaAlbum"] = "pushMessageContentMediaAlbum"

    total_count: int
    """Number of messages in the album"""
    has_photos: bool
    """True, if the album has at least one photo"""
    has_videos: bool
    """True, if the album has at least one video file"""
    has_audios: bool
    """True, if the album has at least one audio file"""
    has_documents: bool
    """True, if the album has at least one document"""
