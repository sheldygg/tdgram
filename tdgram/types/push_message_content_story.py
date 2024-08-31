from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentStory(BaseType):
    """
    A message with a story
    """

    __type__: Literal["pushMessageContentStory"] = "pushMessageContentStory"

    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
