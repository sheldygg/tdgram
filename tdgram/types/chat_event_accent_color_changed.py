from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventAccentColorChanged(BaseType):
    """
    The chat accent color or background custom emoji were changed
    """

    __type__: Literal["chatEventAccentColorChanged"] = "chatEventAccentColorChanged"

    old_accent_color_id: int
    """Previous identifier of chat accent color"""
    old_background_custom_emoji_id: int
    """Previous identifier of the custom emoji; 0 if none"""
    new_accent_color_id: int
    """New identifier of chat accent color"""
    new_background_custom_emoji_id: int
    """New identifier of the custom emoji; 0 if none"""
