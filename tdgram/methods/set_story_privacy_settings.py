from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, StoryPrivacySettings
from .base import BaseMethod


@dataclass(kw_only=True)
class SetStoryPrivacySettings(BaseMethod):
    """
    Changes privacy settings of a story. The method can be called only for stories posted on behalf of the current user and if story.can_be_edited == true
    """

    __type__: Literal["setStoryPrivacySettings"] = "setStoryPrivacySettings"
    __returning_type__ = Ok

    story_id: int
    """Identifier of the story"""
    privacy_settings: StoryPrivacySettings
    """The new privacy settigs for the story"""
