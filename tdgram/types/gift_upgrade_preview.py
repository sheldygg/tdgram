from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UpgradedGiftBackdrop, UpgradedGiftModel, UpgradedGiftSymbol


@dataclass(kw_only=True)
class GiftUpgradePreview(BaseType):
    """
    Contains examples of possible upgraded gifts for the given regular gift
    """

    __type__: Literal["giftUpgradePreview"] = "giftUpgradePreview"

    models: list[UpgradedGiftModel]
    """Examples of possible models that can be chosen for the gift after upgrade"""
    symbols: list[UpgradedGiftSymbol]
    """Examples of possible symbols that can be chosen for the gift after upgrade"""
    backdrops: list[UpgradedGiftBackdrop]
    """Examples of possible backdrops that can be chosen for the gift after upgrade"""
