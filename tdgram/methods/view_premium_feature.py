from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, PremiumFeature
from .base import BaseMethod


@dataclass(kw_only=True)
class ViewPremiumFeature(BaseMethod):
    """
    Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen
    """

    __type__: Literal["viewPremiumFeature"] = "viewPremiumFeature"
    __returning_type__ = Ok

    feature: PremiumFeature
    """The viewed premium feature"""
