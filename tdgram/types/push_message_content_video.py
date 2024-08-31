from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Video


@dataclass(kw_only=True)
class PushMessageContentVideo(BaseType):
    """
    A video message
    """

    __type__: Literal["pushMessageContentVideo"] = "pushMessageContentVideo"

    video: Video | None = None
    """Message content; may be null"""
    caption: str
    """Video caption"""
    is_secret: bool
    """True, if the video is secret"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
