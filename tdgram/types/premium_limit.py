from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PremiumLimitType


@dataclass(kw_only=True)
class PremiumLimit(BaseType):
    """
    Contains information about a limit, increased for Premium users
    """

    __type__: Literal["premiumLimit"] = "premiumLimit"

    type: PremiumLimitType
    """The type of the limit"""
    default_value: int
    """Default value of the limit"""
    premium_value: int
    """Value of the limit for Premium users"""
