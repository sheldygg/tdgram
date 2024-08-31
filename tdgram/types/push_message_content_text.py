from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentText(BaseType):
    """
    A text message
    """

    __type__: Literal["pushMessageContentText"] = "pushMessageContentText"

    text: str
    """Message text"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
