from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto


@dataclass(kw_only=True)
class ChatPhotos(BaseType):
    """
    Contains a list of chat or user profile photos
    """

    __type__: Literal["chatPhotos"] = "chatPhotos"

    total_count: int
    """Total number of photos"""
    photos: list[ChatPhoto]
    """List of photos"""
