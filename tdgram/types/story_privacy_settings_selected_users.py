from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryPrivacySettingsSelectedUsers(BaseType):
    """
    The story can be viewed by certain specified users
    """

    __type__: Literal["storyPrivacySettingsSelectedUsers"] = "storyPrivacySettingsSelectedUsers"

    user_ids: list[int]
    """Identifiers of the users; always unknown and empty for non-owned stories"""
