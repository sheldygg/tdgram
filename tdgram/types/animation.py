from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Minithumbnail, Thumbnail


@dataclass(kw_only=True)
class Animation(BaseType):
    """
    Describes an animation file. The animation must be encoded in GIF or MPEG4 format
    """

    __type__: Literal["animation"] = "animation"

    duration: int
    """Duration of the animation, in seconds; as defined by the sender"""
    width: int
    """Width of the animation"""
    height: int
    """Height of the animation"""
    file_name: str
    """Original name of the file; as defined by the sender"""
    mime_type: str
    """MIME type of the file, usually 'image/gif' or 'video/mp4'"""
    has_stickers: bool
    """True, if stickers were added to the animation. The list of corresponding sticker set can be received using getAttachedStickerSets"""
    minithumbnail: Minithumbnail | None = None
    """Animation minithumbnail; may be null"""
    thumbnail: Thumbnail | None = None
    """Animation thumbnail in JPEG or MPEG4 format; may be null"""
    animation: File
    """File containing the animation"""
