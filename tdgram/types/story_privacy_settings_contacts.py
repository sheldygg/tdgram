from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryPrivacySettingsContacts(BaseType):
    """
    The story can be viewed by all contacts except chosen users
    """

    __type__: Literal["storyPrivacySettingsContacts"] = "storyPrivacySettingsContacts"

    except_user_ids: list[int]
    """User identifiers of the contacts that can't see the story; always unknown and empty for non-owned stories"""
