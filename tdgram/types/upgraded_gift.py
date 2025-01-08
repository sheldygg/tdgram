from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        UpgradedGiftBackdrop,
        UpgradedGiftModel,
        UpgradedGiftOriginalDetails,
        UpgradedGiftSymbol,
    )


@dataclass(kw_only=True)
class UpgradedGift(BaseType):
    """
    Describes an upgraded gift that can be gifted to another user or transferred to TON blockchain as an NFT
    """

    __type__: Literal["upgradedGift"] = "upgradedGift"

    id: int
    """Unique identifier of the gift"""
    title: str
    """The title of the upgraded gift"""
    number: int
    """Unique number of the upgraded gift among gifts upgraded from the same gift"""
    total_upgraded_count: int
    """Total number of gifts that were upgraded from the same gift"""
    max_upgraded_count: int
    """The maximum number of gifts that can be upgraded from the same gift"""
    owner_user_id: int
    """User identifier of the user that owns the upgraded gift; 0 if none"""
    model: UpgradedGiftModel
    """Model of the upgraded gift"""
    symbol: UpgradedGiftSymbol
    """Symbol of the upgraded gift"""
    backdrop: UpgradedGiftBackdrop
    """Backdrop of the upgraded gift"""
    original_details: UpgradedGiftOriginalDetails | None = None
    """Information about the originally sent gift; may be null if unknown"""
