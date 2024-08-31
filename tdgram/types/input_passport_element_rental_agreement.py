from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputPersonalDocument


@dataclass(kw_only=True)
class InputPassportElementRentalAgreement(BaseType):
    """
    A Telegram Passport element to be saved containing the user's rental agreement
    """

    __type__: Literal["inputPassportElementRentalAgreement"] = (
        "inputPassportElementRentalAgreement"
    )

    rental_agreement: InputPersonalDocument
    """The rental agreement to be saved"""
