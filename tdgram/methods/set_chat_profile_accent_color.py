from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatProfileAccentColor(BaseMethod):
    """
    Changes accent color and background custom emoji for profile of a supergroup or channel chat. Requires can_change_info administrator right
    """

    __type__: Literal["setChatProfileAccentColor"] = "setChatProfileAccentColor"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    profile_accent_color_id: int
    """Identifier of the accent color to use for profile; pass -1 if none. The chat must have at least profileAccentColor.min_supergroup_chat_boost_level for supergroups"""
    profile_background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the chat's profile photo background; 0 if none. Use chatBoostLevelFeatures.can_set_profile_background_custom_emoji to check whether a custom emoji can be set"""
