from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryPrivacySettingsEveryone(BaseType):
    """
    The story can be viewed by everyone
    """

    __type__: Literal["storyPrivacySettingsEveryone"] = "storyPrivacySettingsEveryone"

    except_user_ids: list[int]
    """Identifiers of the users that can't see the story; always unknown and empty for non-owned stories"""
