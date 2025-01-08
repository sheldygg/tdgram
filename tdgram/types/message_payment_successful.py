from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessagePaymentSuccessful(BaseType):
    """
    A payment has been sent to a bot or a business account
    """

    __type__: Literal["messagePaymentSuccessful"] = "messagePaymentSuccessful"

    invoice_chat_id: int
    """Identifier of the chat, containing the corresponding invoice message"""
    invoice_message_id: int
    """Identifier of the message with the corresponding invoice; can be 0 or an identifier of a deleted message"""
    currency: str
    """Currency for the price of the product"""
    total_amount: int
    """Total price for the product, in the smallest units of the currency"""
    subscription_until_date: int
    """Point in time (Unix timestamp) when the subscription will expire; 0 if unknown or the payment isn't recurring"""
    is_recurring: bool
    """True, if this is a recurring payment"""
    is_first_recurring: bool
    """True, if this is the first recurring payment"""
    invoice_name: str | None = None
    """Name of the invoice; may be empty if unknown"""
