from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpgradedGiftBackdrop(BaseType):
    """
    Describes a backdrop of an upgraded gift
    """

    __type__: Literal["upgradedGiftBackdrop"] = "upgradedGiftBackdrop"

    name: str
    """Name of the backdrop"""
    center_color: int
    """A color in the center of the backdrop in the RGB format"""
    edge_color: int
    """A color on the edges of the backdrop in the RGB format"""
    symbol_color: int
    """A color to be applied for the symbol in the RGB format"""
    text_color: int
    """A color for the text on the backdrop in the RGB format"""
    rarity_per_mille: int
    """The number of upgraded gift that receive this backdrop for each 1000 gifts upgraded"""
