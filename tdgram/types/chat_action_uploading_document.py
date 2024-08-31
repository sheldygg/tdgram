from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionUploadingDocument(BaseType):
    """
    The user is uploading a document
    """

    __type__: Literal["chatActionUploadingDocument"] = "chatActionUploadingDocument"

    progress: int
    """Upload progress, as a percentage"""
