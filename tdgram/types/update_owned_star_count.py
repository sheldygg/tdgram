from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateOwnedStarCount(BaseType):
    """
    The number of Telegram Stars owned by the current user has changed
    """

    __type__: Literal["updateOwnedStarCount"] = "updateOwnedStarCount"

    star_count: int
    """The new number of Telegram Stars owned"""
