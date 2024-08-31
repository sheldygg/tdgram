from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatStatisticsObjectTypeStory(BaseType):
    """
    Describes a story sent by the chat
    """

    __type__: Literal["chatStatisticsObjectTypeStory"] = "chatStatisticsObjectTypeStory"

    story_id: int
    """Story identifier"""
