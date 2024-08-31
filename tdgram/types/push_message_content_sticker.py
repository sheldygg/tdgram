from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class PushMessageContentSticker(BaseType):
    """
    A message with a sticker
    """

    __type__: Literal["pushMessageContentSticker"] = "pushMessageContentSticker"

    sticker: Sticker | None = None
    """Message content; may be null"""
    emoji: str | None = None
    """Emoji corresponding to the sticker; may be empty"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
