from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeSupergroupCount(BaseType):
    """
    The maximum number of joined supergroups and channels
    """

    __type__: Literal["premiumLimitTypeSupergroupCount"] = "premiumLimitTypeSupergroupCount"
