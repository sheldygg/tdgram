from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BackgroundType, InputBackground, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatBackground(BaseMethod):
    """
    Sets the background in a specific chat. Supported only in private and secret chats with non-deleted users, and in chats with sufficient boost level and can_change_info administrator right
    """

    __type__: Literal["setChatBackground"] = "setChatBackground"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    background: InputBackground | None = None
    """The input background to use; pass null to create a new filled or chat theme background"""
    type: BackgroundType | None = None
    """Background type; pass null to use default background type for the chosen background; backgroundTypeChatTheme isn't supported for private and secret chats."""
    dark_theme_dimming: int
    """Dimming of the background in dark themes, as a percentage; 0-100. Applied only to Wallpaper and Fill types of background"""
    only_for_self: bool
    """Pass true to set background only for self; pass false to set background for all chat users. Always false for backgrounds set in boosted chats. Background can be set for both users only by Telegram Premium users and if set background isn't of the type inputBackgroundPrevious"""
