from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementTypeBankStatement(BaseType):
    """
    A Telegram Passport element containing the user's bank statement
    """

    __type__: Literal["passportElementTypeBankStatement"] = "passportElementTypeBankStatement"
