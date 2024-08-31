from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PhoneNumberCodeTypeVerify(BaseType):
    """
    Verifies ownership of a phone number to be added to the user's Telegram Passport
    """

    __type__: Literal["phoneNumberCodeTypeVerify"] = "phoneNumberCodeTypeVerify"
