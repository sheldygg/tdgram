from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumSourceSettings(BaseType):
    """
    A user opened the Premium features screen from settings
    """

    __type__: Literal["premiumSourceSettings"] = "premiumSourceSettings"
