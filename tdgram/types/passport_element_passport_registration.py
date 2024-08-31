from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PersonalDocument


@dataclass(kw_only=True)
class PassportElementPassportRegistration(BaseType):
    """
    A Telegram Passport element containing the user's passport registration pages
    """

    __type__: Literal["passportElementPassportRegistration"] = (
        "passportElementPassportRegistration"
    )

    passport_registration: PersonalDocument
    """Passport registration pages"""
