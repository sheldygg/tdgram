from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentPaidMedia(BaseType):
    """
    A message with paid media
    """

    __type__: Literal["pushMessageContentPaidMedia"] = "pushMessageContentPaidMedia"

    star_count: int
    """Number of Telegram Stars needed to buy access to the media in the message; 0 for pinned message"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
