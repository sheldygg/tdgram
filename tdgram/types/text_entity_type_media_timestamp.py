from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeMediaTimestamp(BaseType):
    """
    A media timestamp
    """

    __type__: Literal["textEntityTypeMediaTimestamp"] = "textEntityTypeMediaTimestamp"

    media_timestamp: int
    """Timestamp from which a video/audio/video note/voice note/story playing must start, in seconds. The media can be in the content or the link preview of the current message, or in the same places in the replied message"""
