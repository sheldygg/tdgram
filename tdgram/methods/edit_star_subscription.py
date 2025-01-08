from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EditStarSubscription(BaseMethod):
    """
    Cancels or re-enables Telegram Star subscription
    """

    __type__: Literal["editStarSubscription"] = "editStarSubscription"
    __returning_type__ = Ok

    subscription_id: str
    """Identifier of the subscription to change"""
    is_canceled: bool
    """New value of is_canceled"""
