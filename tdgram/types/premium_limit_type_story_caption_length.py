from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeStoryCaptionLength(BaseType):
    """
    The maximum length of captions of sent stories
    """

    __type__: Literal["premiumLimitTypeStoryCaptionLength"] = "premiumLimitTypeStoryCaptionLength"
