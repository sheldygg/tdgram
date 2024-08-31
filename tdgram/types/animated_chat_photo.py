from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File


@dataclass(kw_only=True)
class AnimatedChatPhoto(BaseType):
    """
    Animated variant of a chat photo in MPEG4 format
    """

    __type__: Literal["animatedChatPhoto"] = "animatedChatPhoto"

    length: int
    """Animation width and height"""
    file: File
    """Information about the animation file"""
    main_frame_timestamp: float
    """Timestamp of the frame, used as a static chat photo"""
