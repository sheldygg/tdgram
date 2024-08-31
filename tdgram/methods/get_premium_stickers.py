from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPremiumStickers(BaseMethod):
    """
    Returns premium stickers from regular sticker sets
    """

    __type__: Literal["getPremiumStickers"] = "getPremiumStickers"
    __returning_type__ = Stickers

    limit: int
    """The maximum number of stickers to be returned; 0-100"""
