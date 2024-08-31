from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReuseStarSubscription(BaseMethod):
    """
    Reuses an active subscription and joins the subscribed chat again
    """

    __type__: Literal["reuseStarSubscription"] = "reuseStarSubscription"
    __returning_type__ = Ok

    subscription_id: str
    """Identifier of the subscription"""
