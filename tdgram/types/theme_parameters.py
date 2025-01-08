from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ThemeParameters(BaseType):
    """
    Contains parameters of the application theme
    """

    __type__: Literal["themeParameters"] = "themeParameters"

    background_color: int
    """A color of the background in the RGB format"""
    secondary_background_color: int
    """A secondary color for the background in the RGB format"""
    header_background_color: int
    """A color of the header background in the RGB format"""
    bottom_bar_background_color: int
    """A color of the bottom bar background in the RGB format"""
    section_background_color: int
    """A color of the section background in the RGB format"""
    section_separator_color: int
    """A color of the section separator in the RGB format"""
    text_color: int
    """A color of text in the RGB format"""
    accent_text_color: int
    """An accent color of the text in the RGB format"""
    section_header_text_color: int
    """A color of text on the section headers in the RGB format"""
    subtitle_text_color: int
    """A color of the subtitle text in the RGB format"""
    destructive_text_color: int
    """A color of the text for destructive actions in the RGB format"""
    hint_color: int
    """A color of hints in the RGB format"""
    link_color: int
    """A color of links in the RGB format"""
    button_color: int
    """A color of the buttons in the RGB format"""
    button_text_color: int
    """A color of text on the buttons in the RGB format"""
