from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Date, InputFile


@dataclass(kw_only=True)
class InputIdentityDocument(BaseType):
    """
    An identity document to be saved to Telegram Passport
    """

    __type__: Literal["inputIdentityDocument"] = "inputIdentityDocument"

    number: str
    """Document number; 1-24 characters"""
    expiration_date: Date | None = None
    """Document expiration date; pass null if not applicable"""
    front_side: InputFile
    """Front side of the document"""
    reverse_side: InputFile | None = None
    """Reverse side of the document; only for driver license and identity card; pass null otherwise"""
    selfie: InputFile | None = None
    """Selfie with the document; pass null if unavailable"""
    translation: list[InputFile]
    """List of files containing a certified English translation of the document"""
