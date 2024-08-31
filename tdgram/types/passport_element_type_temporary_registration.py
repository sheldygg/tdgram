from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypeTemporaryRegistration(BaseType):
    """
    A Telegram Passport element containing the user's temporary registration
    """

    __type__: Literal["passportElementTypeTemporaryRegistration"] = (
        "passportElementTypeTemporaryRegistration"
    )
