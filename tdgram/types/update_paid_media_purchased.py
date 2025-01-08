from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdatePaidMediaPurchased(BaseType):
    """
    Paid media were purchased by a user; for bots only
    """

    __type__: Literal["updatePaidMediaPurchased"] = "updatePaidMediaPurchased"

    user_id: int
    """User identifier"""
    payload: str
    """Bot-specified payload for the paid media"""
