from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentPoll(BaseType):
    """
    A message with a poll
    """

    __type__: Literal["pushMessageContentPoll"] = "pushMessageContentPoll"

    question: str
    """Poll question"""
    is_regular: bool
    """True, if the poll is regular and not in quiz mode"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
