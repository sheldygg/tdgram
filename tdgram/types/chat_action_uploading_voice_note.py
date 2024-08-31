from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionUploadingVoiceNote(BaseType):
    """
    The user is uploading a voice note
    """

    __type__: Literal["chatActionUploadingVoiceNote"] = "chatActionUploadingVoiceNote"

    progress: int
    """Upload progress, as a percentage"""
