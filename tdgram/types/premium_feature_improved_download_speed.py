from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureImprovedDownloadSpeed(BaseType):
    """
    Improved download speed
    """

    __type__: Literal["premiumFeatureImprovedDownloadSpeed"] = (
        "premiumFeatureImprovedDownloadSpeed"
    )
