from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionRecordingVideo(BaseType):
    """
    The user is recording a video
    """

    __type__: Literal["chatActionRecordingVideo"] = "chatActionRecordingVideo"
