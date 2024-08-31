from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, PaidMedia, ProductInfo


@dataclass(kw_only=True)
class MessageInvoice(BaseType):
    """
    A message with an invoice from a bot. Use getInternalLink with internalLinkTypeBotStart to share the invoice
    """

    __type__: Literal["messageInvoice"] = "messageInvoice"

    product_info: ProductInfo
    """Information about the product"""
    currency: str
    """Currency for the product price"""
    total_amount: int
    """Product total price in the smallest units of the currency"""
    start_parameter: str
    """Unique invoice bot start_parameter to be passed to getInternalLink"""
    is_test: bool
    """True, if the invoice is a test invoice"""
    need_shipping_address: bool
    """True, if the shipping address must be specified"""
    receipt_message_id: int
    """The identifier of the message with the receipt, after the product has been purchased"""
    paid_media: PaidMedia | None = None
    """Extended media attached to the invoice; may be null if none"""
    paid_media_caption: FormattedText | None = None
    """Extended media caption; may be null if none"""
