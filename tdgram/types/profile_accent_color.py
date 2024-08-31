from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ProfileAccentColors


@dataclass(kw_only=True)
class ProfileAccentColor(BaseType):
    """
    Contains information about supported accent color for user profile photo background
    """

    __type__: Literal["profileAccentColor"] = "profileAccentColor"

    id: int
    """Profile accent color identifier"""
    light_theme_colors: ProfileAccentColors
    """Accent colors expected to be used in light themes"""
    dark_theme_colors: ProfileAccentColors
    """Accent colors expected to be used in dark themes"""
    min_supergroup_chat_boost_level: int
    """The minimum chat boost level required to use the color in a supergroup chat"""
    min_channel_chat_boost_level: int
    """The minimum chat boost level required to use the color in a channel chat"""
