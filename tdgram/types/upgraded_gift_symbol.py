from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class UpgradedGiftSymbol(BaseType):
    """
    Describes a symbol shown on the pattern of an upgraded gift
    """

    __type__: Literal["upgradedGiftSymbol"] = "upgradedGiftSymbol"

    name: str
    """Name of the symbol"""
    sticker: Sticker
    """The sticker representing the upgraded gift"""
    rarity_per_mille: int
    """The number of upgraded gift that receive this symbol for each 1000 gifts upgraded"""
