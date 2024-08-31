from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypeDriverLicense(BaseType):
    """
    A Telegram Passport element containing the user's driver license
    """

    __type__: Literal["passportElementTypeDriverLicense"] = "passportElementTypeDriverLicense"
