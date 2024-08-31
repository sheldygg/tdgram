from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeMissedCall(BaseType):
    """
    An authentication code is delivered by an immediately canceled call to the specified phone number. The last digits of the phone number that calls are the code that must be entered manually by the user
    """

    __type__: Literal["authenticationCodeTypeMissedCall"] = "authenticationCodeTypeMissedCall"

    phone_number_prefix: str
    """Prefix of the phone number from which the call will be made"""
    length: int
    """Number of digits in the code, excluding the prefix"""
