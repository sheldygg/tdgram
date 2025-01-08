from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AccentColor


@dataclass(kw_only=True)
class UpdateAccentColors(BaseType):
    """
    The list of supported accent colors has changed
    """

    __type__: Literal["updateAccentColors"] = "updateAccentColors"

    colors: list[AccentColor]
    """Information about supported colors; colors with identifiers 0 (red), 1 (orange), 2 (purple/violet), 3 (green), 4 (cyan), 5 (blue), 6 (pink) must always be supported"""
    available_accent_color_ids: list[int]
    """The list of accent color identifiers, which can be set through setAccentColor and setChatAccentColor. The colors must be shown in the specified order"""
