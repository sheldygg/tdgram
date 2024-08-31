from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypePassportRegistration(BaseType):
    """
    A Telegram Passport element containing the registration page of the user's passport
    """

    __type__: Literal["passportElementTypePassportRegistration"] = (
        "passportElementTypePassportRegistration"
    )
