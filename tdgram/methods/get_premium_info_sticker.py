from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Sticker
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPremiumInfoSticker(BaseMethod):
    """
    Returns the sticker to be used as representation of the Telegram Premium subscription
    """

    __type__: Literal["getPremiumInfoSticker"] = "getPremiumInfoSticker"
    __returning_type__ = Sticker

    month_count: int
    """Number of months the Telegram Premium subscription will be active"""
