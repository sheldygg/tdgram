from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Background, BackgroundFill


@dataclass(kw_only=True)
class ThemeSettings(BaseType):
    """
    Describes theme settings
    """

    __type__: Literal["themeSettings"] = "themeSettings"

    accent_color: int
    """Theme accent color in ARGB format"""
    background: Background | None = None
    """The background to be used in chats; may be null"""
    outgoing_message_fill: BackgroundFill
    """The fill to be used as a background for outgoing messages"""
    animate_outgoing_message_fill: bool
    """If true, the freeform gradient fill needs to be animated on every sent message"""
    outgoing_message_accent_color: int
    """Accent color of outgoing messages in ARGB format"""
