from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventProfileAccentColorChanged(BaseType):
    """
    The chat's profile accent color or profile background custom emoji were changed
    """

    __type__: Literal["chatEventProfileAccentColorChanged"] = "chatEventProfileAccentColorChanged"

    old_profile_accent_color_id: int
    """Previous identifier of chat's profile accent color; -1 if none"""
    old_profile_background_custom_emoji_id: int
    """Previous identifier of the custom emoji; 0 if none"""
    new_profile_accent_color_id: int
    """New identifier of chat's profile accent color; -1 if none"""
    new_profile_background_custom_emoji_id: int
    """New identifier of the custom emoji; 0 if none"""
