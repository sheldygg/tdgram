from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ApplyPremiumGiftCode(BaseMethod):
    """
    Applies a Telegram Premium gift code
    """

    __type__: Literal["applyPremiumGiftCode"] = "applyPremiumGiftCode"
    __returning_type__ = Ok

    code: str
    """The code to apply"""
