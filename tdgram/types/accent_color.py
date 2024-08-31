from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AccentColor(BaseType):
    """
    Contains information about supported accent color for user/chat name, background of empty chat photo, replies to messages and link previews
    """

    __type__: Literal["accentColor"] = "accentColor"

    id: int
    """Accent color identifier"""
    built_in_accent_color_id: int
    """Identifier of a built-in color to use in places, where only one color is needed; 0-6"""
    light_theme_colors: list[int]
    """The list of 1-3 colors in RGB format, describing the accent color, as expected to be shown in light themes"""
    dark_theme_colors: list[int]
    """The list of 1-3 colors in RGB format, describing the accent color, as expected to be shown in dark themes"""
    min_channel_chat_boost_level: int
    """The minimum chat boost level required to use the color in a channel chat"""
