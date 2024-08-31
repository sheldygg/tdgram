from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import VideoNote


@dataclass(kw_only=True)
class MessageVideoNote(BaseType):
    """
    A video note message
    """

    __type__: Literal["messageVideoNote"] = "messageVideoNote"

    video_note: VideoNote
    """The video note description"""
    is_viewed: bool
    """True, if at least one of the recipients has viewed the video note"""
    is_secret: bool
    """True, if the video note thumbnail must be blurred and the video note must be shown only while tapped"""
