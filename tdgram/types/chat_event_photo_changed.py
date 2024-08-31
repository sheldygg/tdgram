from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto


@dataclass(kw_only=True)
class ChatEventPhotoChanged(BaseType):
    """
    The chat photo was changed
    """

    __type__: Literal["chatEventPhotoChanged"] = "chatEventPhotoChanged"

    old_photo: ChatPhoto | None = None
    """Previous chat photo value; may be null"""
    new_photo: ChatPhoto | None = None
    """New chat photo value; may be null"""
