from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PremiumGiftCodeInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckPremiumGiftCode(BaseMethod):
    """
    Return information about a Telegram Premium gift code
    """

    __type__: Literal["checkPremiumGiftCode"] = "checkPremiumGiftCode"
    __returning_type__ = PremiumGiftCodeInfo

    code: str
    """The code to check"""
