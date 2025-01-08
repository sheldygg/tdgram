from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AffiliateProgramParameters, StarAmount


@dataclass(kw_only=True)
class AffiliateProgramInfo(BaseType):
    """
    Contains information about an active affiliate program
    """

    __type__: Literal["affiliateProgramInfo"] = "affiliateProgramInfo"

    parameters: AffiliateProgramParameters
    """Parameters of the affiliate program"""
    end_date: int
    """Point in time (Unix timestamp) when the affiliate program will be closed; 0 if the affiliate program isn't scheduled to be closed."""
    daily_revenue_per_user_amount: StarAmount
    """The amount of daily revenue per user in Telegram Stars of the bot that created the affiliate program"""
