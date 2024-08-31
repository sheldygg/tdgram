from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypeIdentityCard(BaseType):
    """
    A Telegram Passport element containing the user's identity card
    """

    __type__: Literal["passportElementTypeIdentityCard"] = "passportElementTypeIdentityCard"
