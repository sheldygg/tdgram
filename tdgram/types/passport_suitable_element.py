from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PassportElementType


@dataclass(kw_only=True)
class PassportSuitableElement(BaseType):
    """
    Contains information about a Telegram Passport element that was requested by a service
    """

    __type__: Literal["passportSuitableElement"] = "passportSuitableElement"

    type: PassportElementType
    """Type of the element"""
    is_selfie_required: bool
    """True, if a selfie is required with the identity document"""
    is_translation_required: bool
    """True, if a certified English translation is required with the document"""
    is_native_name_required: bool
    """True, if personal details must include the user's name in the language of their country of residence"""
