from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ThemeSettings


@dataclass(kw_only=True)
class ChatTheme(BaseType):
    """
    Describes a chat theme
    """

    __type__: Literal["chatTheme"] = "chatTheme"

    name: str
    """Theme name"""
    light_settings: ThemeSettings
    """Theme settings for a light chat theme"""
    dark_settings: ThemeSettings
    """Theme settings for a dark chat theme"""
