from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TelegramPaymentPurpose


@dataclass(kw_only=True)
class InputInvoiceTelegram(BaseType):
    """
    An invoice for a payment toward Telegram; must not be used in the in-store apps
    """

    __type__: Literal["inputInvoiceTelegram"] = "inputInvoiceTelegram"

    purpose: TelegramPaymentPurpose
    """Transaction purpose"""
