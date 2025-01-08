from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import GiftUpgradePreview
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGiftUpgradePreview(BaseMethod):
    """
    Returns examples of possible upgraded gifts for a regular gift
    """

    __type__: Literal["getGiftUpgradePreview"] = "getGiftUpgradePreview"
    __returning_type__ = GiftUpgradePreview

    gift_id: int
    """Identifier of the gift"""
