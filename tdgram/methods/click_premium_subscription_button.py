from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClickPremiumSubscriptionButton(BaseMethod):
    """
    Informs TDLib that the user clicked Premium subscription button on the Premium features screen
    """

    __type__: Literal["clickPremiumSubscriptionButton"] = "clickPremiumSubscriptionButton"
    __returning_type__ = Ok
