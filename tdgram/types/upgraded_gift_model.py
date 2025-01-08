from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class UpgradedGiftModel(BaseType):
    """
    Describes a model of an upgraded gift
    """

    __type__: Literal["upgradedGiftModel"] = "upgradedGiftModel"

    name: str
    """Name of the model"""
    sticker: Sticker
    """The sticker representing the upgraded gift"""
    rarity_per_mille: int
    """The number of upgraded gift that receive this model for each 1000 gifts upgraded"""
