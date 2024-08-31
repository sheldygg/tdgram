from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ForumTopicIcon(BaseType):
    """
    Describes a forum topic icon
    """

    __type__: Literal["forumTopicIcon"] = "forumTopicIcon"

    color: int
    """Color of the topic icon in RGB format"""
    custom_emoji_id: int
    """Unique identifier of the custom emoji shown on the topic icon; 0 if none"""
