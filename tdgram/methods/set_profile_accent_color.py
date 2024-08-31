from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetProfileAccentColor(BaseMethod):
    """
    Changes accent color and background custom emoji for profile of the current user; for Telegram Premium users only
    """

    __type__: Literal["setProfileAccentColor"] = "setProfileAccentColor"
    __returning_type__ = Ok

    profile_accent_color_id: int
    """Identifier of the accent color to use for profile; pass -1 if none"""
    profile_background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the user's profile photo background; 0 if none"""
