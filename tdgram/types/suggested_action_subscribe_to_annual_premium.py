from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionSubscribeToAnnualPremium(BaseType):
    """
    Suggests the user to subscribe to the Premium subscription with annual payments
    """

    __type__: Literal["suggestedActionSubscribeToAnnualPremium"] = (
        "suggestedActionSubscribeToAnnualPremium"
    )
