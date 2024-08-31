from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StarPaymentOptions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStarGiftPaymentOptions(BaseMethod):
    """
    Returns available options for Telegram Stars gifting
    """

    __type__: Literal["getStarGiftPaymentOptions"] = "getStarGiftPaymentOptions"
    __returning_type__ = StarPaymentOptions

    user_id: int
    """Identifier of the user that will receive Telegram Stars; pass 0 to get options for an unspecified user"""
