from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Backgrounds
from .base import BaseMethod


@dataclass(kw_only=True)
class GetInstalledBackgrounds(BaseMethod):
    """
    Returns backgrounds installed by the user
    """

    __type__: Literal["getInstalledBackgrounds"] = "getInstalledBackgrounds"
    __returning_type__ = Backgrounds

    for_dark_theme: bool
    """Pass true to order returned backgrounds for a dark theme"""
