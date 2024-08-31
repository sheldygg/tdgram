from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionRecordingVideoNote(BaseType):
    """
    The user is recording a video note
    """

    __type__: Literal["chatActionRecordingVideoNote"] = "chatActionRecordingVideoNote"
