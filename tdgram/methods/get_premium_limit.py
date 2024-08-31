from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PremiumLimit, PremiumLimitType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPremiumLimit(BaseMethod):
    """
    Returns information about a limit, increased for Premium users. Returns a 404 error if the limit is unknown
    """

    __type__: Literal["getPremiumLimit"] = "getPremiumLimit"
    __returning_type__ = PremiumLimit

    limit_type: PremiumLimitType
    """Type of the limit"""
