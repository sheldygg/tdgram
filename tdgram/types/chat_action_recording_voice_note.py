from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionRecordingVoiceNote(BaseType):
    """
    The user is recording a voice note
    """

    __type__: Literal["chatActionRecordingVoiceNote"] = "chatActionRecordingVoiceNote"
