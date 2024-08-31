from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class PushMessageContentPhoto(BaseType):
    """
    A photo message
    """

    __type__: Literal["pushMessageContentPhoto"] = "pushMessageContentPhoto"

    photo: Photo | None = None
    """Message content; may be null"""
    caption: str
    """Photo caption"""
    is_secret: bool
    """True, if the photo is secret"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
