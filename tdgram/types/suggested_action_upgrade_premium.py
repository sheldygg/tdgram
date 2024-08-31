from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionUpgradePremium(BaseType):
    """
    Suggests the user to upgrade the Premium subscription from monthly payments to annual payments
    """

    __type__: Literal["suggestedActionUpgradePremium"] = "suggestedActionUpgradePremium"
