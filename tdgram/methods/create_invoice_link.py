from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl, InputMessageContent
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateInvoiceLink(BaseMethod):
    """
    Creates a link for the given invoice; for bots only
    """

    __type__: Literal["createInvoiceLink"] = "createInvoiceLink"
    __returning_type__ = HttpUrl

    invoice: InputMessageContent
    """Information about the invoice of the type inputMessageInvoice"""
