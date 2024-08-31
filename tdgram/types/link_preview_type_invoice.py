from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewTypeInvoice(BaseType):
    """
    The link is a link to an invoice
    """

    __type__: Literal["linkPreviewTypeInvoice"] = "linkPreviewTypeInvoice"
