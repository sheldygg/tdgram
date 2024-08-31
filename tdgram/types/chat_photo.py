from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AnimatedChatPhoto, ChatPhotoSticker, Minithumbnail, PhotoSize


@dataclass(kw_only=True)
class ChatPhoto(BaseType):
    """
    Describes a chat or user profile photo
    """

    __type__: Literal["chatPhoto"] = "chatPhoto"

    id: int
    """Unique photo identifier"""
    added_date: int
    """Point in time (Unix timestamp) when the photo has been added"""
    minithumbnail: Minithumbnail | None = None
    """Photo minithumbnail; may be null"""
    sizes: list[PhotoSize]
    """Available variants of the photo in JPEG format, in different size"""
    animation: AnimatedChatPhoto | None = None
    """A big (up to 1280x1280) animated variant of the photo in MPEG4 format; may be null"""
    small_animation: AnimatedChatPhoto | None = None
    """A small (160x160) animated variant of the photo in MPEG4 format; may be null even the big animation is available"""
    sticker: ChatPhotoSticker | None = None
    """Sticker-based version of the chat photo; may be null"""
