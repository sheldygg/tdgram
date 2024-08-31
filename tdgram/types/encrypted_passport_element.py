from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import DatedFile, PassportElementType


@dataclass(kw_only=True)
class EncryptedPassportElement(BaseType):
    """
    Contains information about an encrypted Telegram Passport element; for bots only
    """

    __type__: Literal["encryptedPassportElement"] = "encryptedPassportElement"

    type: PassportElementType
    """Type of Telegram Passport element"""
    data: bytes
    """Encrypted JSON-encoded data about the user"""
    front_side: DatedFile
    """The front side of an identity document"""
    reverse_side: DatedFile | None = None
    """The reverse side of an identity document; may be null"""
    selfie: DatedFile | None = None
    """Selfie with the document; may be null"""
    translation: list[DatedFile]
    """List of files containing a certified English translation of the document"""
    files: list[DatedFile]
    """List of attached files"""
    value: str
    """Unencrypted data, phone number or email address"""
    hash: str
    """Hash of the entire element"""
