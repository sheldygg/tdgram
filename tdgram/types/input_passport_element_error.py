from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputPassportElementErrorSource, PassportElementType


@dataclass(kw_only=True)
class InputPassportElementError(BaseType):
    """
    Contains the description of an error in a Telegram Passport element; for bots only
    """

    __type__: Literal["inputPassportElementError"] = "inputPassportElementError"

    type: PassportElementType
    """Type of Telegram Passport element that has the error"""
    message: str
    """Error message"""
    source: InputPassportElementErrorSource
    """Error source"""
