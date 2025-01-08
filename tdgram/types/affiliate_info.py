from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarAmount


@dataclass(kw_only=True)
class AffiliateInfo(BaseType):
    """
    Contains information about an affiliate that received commission from a Telegram Star transaction
    """

    __type__: Literal["affiliateInfo"] = "affiliateInfo"

    commission_per_mille: int
    """The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the program owner"""
    affiliate_chat_id: int
    """Identifier of the chat which received the commission"""
    star_amount: StarAmount
    """The amount of Telegram Stars that were received by the affiliate; can be negative for refunds"""
