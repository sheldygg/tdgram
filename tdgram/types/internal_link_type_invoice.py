from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeInvoice(BaseType):
    """
    The link is a link to an invoice. Call getPaymentForm with the given invoice name to process the link
    """

    __type__: Literal["internalLinkTypeInvoice"] = "internalLinkTypeInvoice"

    invoice_name: str
    """Name of the invoice"""
