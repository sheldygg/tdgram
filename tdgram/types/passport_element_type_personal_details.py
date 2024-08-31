from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypePersonalDetails(BaseType):
    """
    A Telegram Passport element containing the user's personal details
    """

    __type__: Literal["passportElementTypePersonalDetails"] = "passportElementTypePersonalDetails"
