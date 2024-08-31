from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class MessagePaymentRefunded(BaseType):
    """
    A payment has been refunded
    """

    __type__: Literal["messagePaymentRefunded"] = "messagePaymentRefunded"

    owner_id: MessageSender
    """Identifier of the previous owner of the Telegram Stars that refunds them"""
    currency: str
    """Currency for the price of the product"""
    total_amount: int
    """Total price for the product, in the smallest units of the currency"""
    invoice_payload: bytes
    """Invoice payload; only for bots"""
    telegram_payment_charge_id: str
    """Telegram payment identifier"""
    provider_payment_charge_id: str
    """Provider payment identifier"""
