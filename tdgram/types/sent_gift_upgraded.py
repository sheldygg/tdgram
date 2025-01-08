from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UpgradedGift


@dataclass(kw_only=True)
class SentGiftUpgraded(BaseType):
    """
    Upgraded gift
    """

    __type__: Literal["sentGiftUpgraded"] = "sentGiftUpgraded"

    gift: UpgradedGift
    """The gift"""
