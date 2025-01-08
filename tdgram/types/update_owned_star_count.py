from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarAmount


@dataclass(kw_only=True)
class UpdateOwnedStarCount(BaseType):
    """
    The number of Telegram Stars owned by the current user has changed
    """

    __type__: Literal["updateOwnedStarCount"] = "updateOwnedStarCount"

    star_amount: StarAmount
    """The new amount of owned Telegram Stars"""
