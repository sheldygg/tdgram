from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PaidMedia


@dataclass(kw_only=True)
class StarTransactionPartnerBusiness(BaseType):
    """
    The transaction is a transaction with a business account
    """

    __type__: Literal["starTransactionPartnerBusiness"] = "starTransactionPartnerBusiness"

    user_id: int
    """Identifier of the business account user"""
    media: list[PaidMedia]
    """The bought media if the trancastion wasn't refunded"""
