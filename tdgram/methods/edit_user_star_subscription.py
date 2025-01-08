from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EditUserStarSubscription(BaseMethod):
    """
    Cancels or re-enables Telegram Star subscription for a user; for bots only
    """

    __type__: Literal["editUserStarSubscription"] = "editUserStarSubscription"
    __returning_type__ = Ok

    user_id: int
    """User identifier"""
    telegram_payment_charge_id: str
    """Telegram payment identifier of the subscription"""
    is_canceled: bool
    """Pass true to cancel the subscription; pass false to allow the user to enable it"""
