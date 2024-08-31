from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionUploadingPhoto(BaseType):
    """
    The user is uploading a photo
    """

    __type__: Literal["chatActionUploadingPhoto"] = "chatActionUploadingPhoto"

    progress: int
    """Upload progress, as a percentage"""
