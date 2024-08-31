from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypeInternalPassport(BaseType):
    """
    A Telegram Passport element containing the user's internal passport
    """

    __type__: Literal["passportElementTypeInternalPassport"] = (
        "passportElementTypeInternalPassport"
    )
