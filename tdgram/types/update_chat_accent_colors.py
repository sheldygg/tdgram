from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatAccentColors(BaseType):
    """
    Chat accent colors have changed
    """

    __type__: Literal["updateChatAccentColors"] = "updateChatAccentColors"

    chat_id: int
    """Chat identifier"""
    accent_color_id: int
    """The new chat accent color identifier"""
    background_custom_emoji_id: int
    """The new identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none"""
    profile_accent_color_id: int
    """The new chat profile accent color identifier; -1 if none"""
    profile_background_custom_emoji_id: int
    """The new identifier of a custom emoji to be shown on the profile background; 0 if none"""
