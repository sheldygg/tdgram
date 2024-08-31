from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Background


@dataclass(kw_only=True)
class ChatBackground(BaseType):
    """
    Describes a background set for a specific chat
    """

    __type__: Literal["chatBackground"] = "chatBackground"

    background: Background
    """The background"""
    dark_theme_dimming: int
    """Dimming of the background in dark themes, as a percentage; 0-100. Applied only to Wallpaper and Fill types of background"""
