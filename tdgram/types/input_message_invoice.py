from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, InputPaidMedia, Invoice


@dataclass(kw_only=True)
class InputMessageInvoice(BaseType):
    """
    A message with an invoice; can be used only by bots
    """

    __type__: Literal["inputMessageInvoice"] = "inputMessageInvoice"

    invoice: Invoice
    """Invoice"""
    title: str
    """Product title; 1-32 characters"""
    description: str
    """Product description; 0-255 characters"""
    photo_url: str
    """Product photo URL; optional"""
    photo_size: int
    """Product photo size"""
    photo_width: int
    """Product photo width"""
    photo_height: int
    """Product photo height"""
    payload: bytes
    """The invoice payload"""
    provider_token: str | None = None
    """Payment provider token; may be empty for payments in Telegram Stars"""
    provider_data: str
    """JSON-encoded data about the invoice, which will be shared with the payment provider"""
    start_parameter: str
    """Unique invoice bot deep link parameter for the generation of this invoice. If empty, it would be possible to pay directly from forwards of the invoice message"""
    paid_media: InputPaidMedia | None = None
    """The content of paid media attached to the invoice; pass null if none"""
    paid_media_caption: FormattedText | None = None
    """Paid media caption; pass null to use an empty caption; 0-getOption('message_caption_length_max') characters"""
