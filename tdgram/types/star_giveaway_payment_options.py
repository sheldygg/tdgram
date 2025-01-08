from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarGiveawayPaymentOption


@dataclass(kw_only=True)
class StarGiveawayPaymentOptions(BaseType):
    """
    Contains a list of options for creating Telegram Star giveaway
    """

    __type__: Literal["starGiveawayPaymentOptions"] = "starGiveawayPaymentOptions"

    options: list[StarGiveawayPaymentOption]
    """The list of options"""
