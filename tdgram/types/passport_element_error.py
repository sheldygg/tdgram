from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PassportElementErrorSource, PassportElementType


@dataclass(kw_only=True)
class PassportElementError(BaseType):
    """
    Contains the description of an error in a Telegram Passport element
    """

    __type__: Literal["passportElementError"] = "passportElementError"

    type: PassportElementType
    """Type of the Telegram Passport element which has the error"""
    message: str
    """Error message"""
    source: PassportElementErrorSource
    """Error source"""
