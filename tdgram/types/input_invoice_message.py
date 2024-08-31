from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputInvoiceMessage(BaseType):
    """
    An invoice from a message of the type messageInvoice or paid media purchase from messagePaidMedia
    """

    __type__: Literal["inputInvoiceMessage"] = "inputInvoiceMessage"

    chat_id: int
    """Chat identifier of the message"""
    message_id: int
    """Message identifier"""
