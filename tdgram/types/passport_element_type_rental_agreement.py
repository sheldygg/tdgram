from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypeRentalAgreement(BaseType):
    """
    A Telegram Passport element containing the user's rental agreement
    """

    __type__: Literal["passportElementTypeRentalAgreement"] = "passportElementTypeRentalAgreement"
