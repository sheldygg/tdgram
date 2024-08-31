from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PersonalDocument


@dataclass(kw_only=True)
class PassportElementRentalAgreement(BaseType):
    """
    A Telegram Passport element containing the user's rental agreement
    """

    __type__: Literal["passportElementRentalAgreement"] = "passportElementRentalAgreement"

    rental_agreement: PersonalDocument
    """Rental agreement"""
