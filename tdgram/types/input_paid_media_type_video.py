from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPaidMediaTypeVideo(BaseType):
    """
    The media is a video
    """

    __type__: Literal["inputPaidMediaTypeVideo"] = "inputPaidMediaTypeVideo"

    duration: int
    """Duration of the video, in seconds"""
    supports_streaming: bool
    """True, if the video is supposed to be streamed"""
