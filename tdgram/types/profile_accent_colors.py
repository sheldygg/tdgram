from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ProfileAccentColors(BaseType):
    """
    Contains information about supported accent colors for user profile photo background in RGB format
    """

    __type__: Literal["profileAccentColors"] = "profileAccentColors"

    palette_colors: list[int]
    """The list of 1-2 colors in RGB format, describing the colors, as expected to be shown in the color palette settings"""
    background_colors: list[int]
    """The list of 1-2 colors in RGB format, describing the colors, as expected to be used for the profile photo background"""
    story_colors: list[int]
    """The list of 2 colors in RGB format, describing the colors of the gradient to be used for the unread active story indicator around profile photo"""
