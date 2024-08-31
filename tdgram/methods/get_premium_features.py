from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PremiumFeatures, PremiumSource
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPremiumFeatures(BaseMethod):
    """
    Returns information about features, available to Premium users
    """

    __type__: Literal["getPremiumFeatures"] = "getPremiumFeatures"
    __returning_type__ = PremiumFeatures

    source: PremiumSource | None = None
    """Source of the request; pass null if the method is called from some non-standard source"""
