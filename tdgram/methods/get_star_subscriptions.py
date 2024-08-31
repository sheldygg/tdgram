from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StarSubscriptions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStarSubscriptions(BaseMethod):
    """
    Returns the list of Telegram Star subscriptions for the current user
    """

    __type__: Literal["getStarSubscriptions"] = "getStarSubscriptions"
    __returning_type__ = StarSubscriptions

    only_expiring: bool
    """Pass true to receive only expiring subscriptions for which there are no enough Telegram Stars to extend"""
    offset: str
    """Offset of the first subscription to return as received from the previous request; use empty string to get the first chunk of results"""
