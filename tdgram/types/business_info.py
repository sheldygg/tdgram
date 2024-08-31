from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        BusinessAwayMessageSettings,
        BusinessGreetingMessageSettings,
        BusinessLocation,
        BusinessOpeningHours,
        BusinessStartPage,
    )


@dataclass(kw_only=True)
class BusinessInfo(BaseType):
    """
    Contains information about a Telegram Business account
    """

    __type__: Literal["businessInfo"] = "businessInfo"

    location: BusinessLocation | None = None
    """Location of the business; may be null if none"""
    opening_hours: BusinessOpeningHours | None = None
    """Opening hours of the business; may be null if none. The hours are guaranteed to be valid and has already been split by week days"""
    local_opening_hours: BusinessOpeningHours | None = None
    """Opening hours of the business in the local time; may be null if none. The hours are guaranteed to be valid and has already been split by week days."""
    next_open_in: int
    """Time left before the business will open the next time, in seconds; 0 if unknown. An updateUserFullInfo update is not triggered when value of this field changes"""
    next_close_in: int
    """Time left before the business will close the next time, in seconds; 0 if unknown. An updateUserFullInfo update is not triggered when value of this field changes"""
    greeting_message_settings: BusinessGreetingMessageSettings | None = None
    """The greeting message; may be null if none or the Business account is not of the current user"""
    away_message_settings: BusinessAwayMessageSettings | None = None
    """The away message; may be null if none or the Business account is not of the current user"""
    start_page: BusinessStartPage | None = None
    """Information about start page of the account; may be null if none"""
