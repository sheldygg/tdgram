from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Minithumbnail, Thumbnail


@dataclass(kw_only=True)
class Video(BaseType):
    """
    Describes a video file
    """

    __type__: Literal["video"] = "video"

    duration: int
    """Duration of the video, in seconds; as defined by the sender"""
    width: int
    """Video width; as defined by the sender"""
    height: int
    """Video height; as defined by the sender"""
    file_name: str
    """Original name of the file; as defined by the sender"""
    mime_type: str
    """MIME type of the file; as defined by the sender"""
    has_stickers: bool
    """True, if stickers were added to the video. The list of corresponding sticker sets can be received using getAttachedStickerSets"""
    supports_streaming: bool
    """True, if the video is supposed to be streamed"""
    minithumbnail: Minithumbnail | None = None
    """Video minithumbnail; may be null"""
    thumbnail: Thumbnail | None = None
    """Video thumbnail in JPEG or MPEG4 format; as defined by the sender; may be null"""
    video: File
    """File containing the video"""
