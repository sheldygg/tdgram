from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatAccentColor(BaseMethod):
    """
    Changes accent color and background custom emoji of a channel chat. Requires can_change_info administrator right
    """

    __type__: Literal["setChatAccentColor"] = "setChatAccentColor"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    accent_color_id: int
    """Identifier of the accent color to use. The chat must have at least accentColor.min_channel_chat_boost_level boost level to pass the corresponding color"""
    background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none. Use chatBoostLevelFeatures.can_set_background_custom_emoji to check whether a custom emoji can be set"""
