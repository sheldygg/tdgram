from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PremiumStoryFeature


@dataclass(kw_only=True)
class PremiumSourceStoryFeature(BaseType):
    """
    A user tried to use a Premium story feature
    """

    __type__: Literal["premiumSourceStoryFeature"] = "premiumSourceStoryFeature"

    feature: PremiumStoryFeature
    """The used feature"""
