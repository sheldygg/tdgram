from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetAccentColor(BaseMethod):
    """
    Changes accent color and background custom emoji for the current user; for Telegram Premium users only
    """

    __type__: Literal["setAccentColor"] = "setAccentColor"
    __returning_type__ = Ok

    accent_color_id: int
    """Identifier of the accent color to use"""
    background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none"""
