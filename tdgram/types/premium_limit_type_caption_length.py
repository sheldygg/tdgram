from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeCaptionLength(BaseType):
    """
    The maximum length of sent media caption
    """

    __type__: Literal["premiumLimitTypeCaptionLength"] = "premiumLimitTypeCaptionLength"
