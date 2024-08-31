from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypeEmailAddress(BaseType):
    """
    A Telegram Passport element containing the user's email address
    """

    __type__: Literal["passportElementTypeEmailAddress"] = "passportElementTypeEmailAddress"
