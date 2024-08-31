from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PremiumFeature


@dataclass(kw_only=True)
class PremiumSourceFeature(BaseType):
    """
    A user tried to use a Premium feature
    """

    __type__: Literal["premiumSourceFeature"] = "premiumSourceFeature"

    feature: PremiumFeature
    """The used feature"""
