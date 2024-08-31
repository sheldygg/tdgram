from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionUploadingVideo(BaseType):
    """
    The user is uploading a video
    """

    __type__: Literal["chatActionUploadingVideo"] = "chatActionUploadingVideo"

    progress: int
    """Upload progress, as a percentage"""
