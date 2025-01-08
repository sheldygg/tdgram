from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile, InputThumbnail, MessageSelfDestructType


@dataclass(kw_only=True)
class InputMessageVideoNote(BaseType):
    """
    A video note message
    """

    __type__: Literal["inputMessageVideoNote"] = "inputMessageVideoNote"

    video_note: InputFile
    """Video note to be sent. The video is expected to be encoded to MPEG4 format with H.264 codec and have no data outside of the visible circle"""
    thumbnail: InputThumbnail | None = None
    """Video thumbnail; may be null if empty; pass null to skip thumbnail uploading"""
    duration: int
    """Duration of the video, in seconds; 0-60"""
    length: int
    """Video width and height; must be positive and not greater than 640"""
    self_destruct_type: MessageSelfDestructType | None = None
    """Video note self-destruct type; may be null if none; pass null if none; private chats only"""
