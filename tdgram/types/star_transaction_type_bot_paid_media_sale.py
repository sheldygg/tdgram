from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AffiliateInfo, PaidMedia


@dataclass(kw_only=True)
class StarTransactionTypeBotPaidMediaSale(BaseType):
    """
    The transaction is a sale of paid media by the bot or a business account managed by the bot; for bots only
    """

    __type__: Literal["starTransactionTypeBotPaidMediaSale"] = (
        "starTransactionTypeBotPaidMediaSale"
    )

    user_id: int
    """Identifier of the user that bought the media"""
    media: list[PaidMedia]
    """The bought media"""
    payload: str
    """Bot-provided payload"""
    affiliate: AffiliateInfo | None = None
    """Information about the affiliate which received commission from the transaction; may be null if none"""
