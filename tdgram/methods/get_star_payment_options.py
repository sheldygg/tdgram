from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StarPaymentOptions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStarPaymentOptions(BaseMethod):
    """
    Returns available options for Telegram Stars purchase
    """

    __type__: Literal["getStarPaymentOptions"] = "getStarPaymentOptions"
    __returning_type__ = StarPaymentOptions
