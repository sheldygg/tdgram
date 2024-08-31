from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import VideoNote


@dataclass(kw_only=True)
class PushMessageContentVideoNote(BaseType):
    """
    A video note message
    """

    __type__: Literal["pushMessageContentVideoNote"] = "pushMessageContentVideoNote"

    video_note: VideoNote | None = None
    """Message content; may be null"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
