from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Date, DatedFile


@dataclass(kw_only=True)
class IdentityDocument(BaseType):
    """
    An identity document
    """

    __type__: Literal["identityDocument"] = "identityDocument"

    number: str
    """Document number; 1-24 characters"""
    expiration_date: Date | None = None
    """Document expiration date; may be null if not applicable"""
    front_side: DatedFile
    """Front side of the document"""
    reverse_side: DatedFile | None = None
    """Reverse side of the document; only for driver license and identity card; may be null"""
    selfie: DatedFile | None = None
    """Selfie with the document; may be null"""
    translation: list[DatedFile]
    """List of files containing a certified English translation of the document"""
