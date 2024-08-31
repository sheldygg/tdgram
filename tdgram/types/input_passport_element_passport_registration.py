from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputPersonalDocument


@dataclass(kw_only=True)
class InputPassportElementPassportRegistration(BaseType):
    """
    A Telegram Passport element to be saved containing the user's passport registration
    """

    __type__: Literal["inputPassportElementPassportRegistration"] = (
        "inputPassportElementPassportRegistration"
    )

    passport_registration: InputPersonalDocument
    """The passport registration page to be saved"""
