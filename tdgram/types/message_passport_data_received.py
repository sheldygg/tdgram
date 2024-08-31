from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EncryptedCredentials, EncryptedPassportElement


@dataclass(kw_only=True)
class MessagePassportDataReceived(BaseType):
    """
    Telegram Passport data has been received; for bots only
    """

    __type__: Literal["messagePassportDataReceived"] = "messagePassportDataReceived"

    elements: list[EncryptedPassportElement]
    """List of received Telegram Passport elements"""
    credentials: EncryptedCredentials
    """Encrypted data credentials"""
