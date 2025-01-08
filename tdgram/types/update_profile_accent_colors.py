from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ProfileAccentColor


@dataclass(kw_only=True)
class UpdateProfileAccentColors(BaseType):
    """
    The list of supported accent colors for user profiles has changed
    """

    __type__: Literal["updateProfileAccentColors"] = "updateProfileAccentColors"

    colors: list[ProfileAccentColor]
    """Information about supported colors"""
    available_accent_color_ids: list[int]
    """The list of accent color identifiers, which can be set through setProfileAccentColor and setChatProfileAccentColor. The colors must be shown in the specified order"""
