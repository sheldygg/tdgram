from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryPrivacySettingsCloseFriends(BaseType):
    """
    The story can be viewed by all close friends
    """

    __type__: Literal["storyPrivacySettingsCloseFriends"] = "storyPrivacySettingsCloseFriends"
