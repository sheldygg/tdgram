from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryOriginHiddenUser(BaseType):
    """
    The original story was sent by an unknown user
    """

    __type__: Literal["storyOriginHiddenUser"] = "storyOriginHiddenUser"

    sender_name: str
    """Name of the story sender"""
