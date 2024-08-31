from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputInvoiceName(BaseType):
    """
    An invoice from a link of the type internalLinkTypeInvoice
    """

    __type__: Literal["inputInvoiceName"] = "inputInvoiceName"

    name: str
    """Name of the invoice"""
