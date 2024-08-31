from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PremiumLimitType


@dataclass(kw_only=True)
class PremiumSourceLimitExceeded(BaseType):
    """
    A limit was exceeded
    """

    __type__: Literal["premiumSourceLimitExceeded"] = "premiumSourceLimitExceeded"

    limit_type: PremiumLimitType
    """Type of the exceeded limit"""
