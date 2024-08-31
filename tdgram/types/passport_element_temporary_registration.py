from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PersonalDocument


@dataclass(kw_only=True)
class PassportElementTemporaryRegistration(BaseType):
    """
    A Telegram Passport element containing the user's temporary registration
    """

    __type__: Literal["passportElementTemporaryRegistration"] = (
        "passportElementTemporaryRegistration"
    )

    temporary_registration: PersonalDocument
    """Temporary registration"""
