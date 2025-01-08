from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Minithumbnail, Thumbnail


@dataclass(kw_only=True)
class StoryVideo(BaseType):
    """
    Describes a video file sent in a story
    """

    __type__: Literal["storyVideo"] = "storyVideo"

    duration: float
    """Duration of the video, in seconds"""
    width: int
    """Video width"""
    height: int
    """Video height"""
    has_stickers: bool
    """True, if stickers were added to the video. The list of corresponding sticker sets can be received using getAttachedStickerSets"""
    is_animation: bool
    """True, if the video has no sound"""
    minithumbnail: Minithumbnail | None = None
    """Video minithumbnail; may be null"""
    thumbnail: Thumbnail | None = None
    """Video thumbnail in JPEG or MPEG4 format; may be null"""
    preload_prefix_size: int
    """Size of file prefix, which is expected to be preloaded, in bytes"""
    cover_frame_timestamp: float
    """Timestamp of the frame used as video thumbnail"""
    video: File
    """File containing the video"""
