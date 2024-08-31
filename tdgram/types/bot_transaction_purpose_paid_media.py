from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PaidMedia


@dataclass(kw_only=True)
class BotTransactionPurposePaidMedia(BaseType):
    """
    Paid media were bought
    """

    __type__: Literal["botTransactionPurposePaidMedia"] = "botTransactionPurposePaidMedia"

    media: list[PaidMedia]
    """The bought media if the trancastion wasn't refunded"""
