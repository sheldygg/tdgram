from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PremiumState
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPremiumState(BaseMethod):
    """
    Returns state of Telegram Premium subscription and promotion videos for Premium features
    """

    __type__: Literal["getPremiumState"] = "getPremiumState"
    __returning_type__ = PremiumState
