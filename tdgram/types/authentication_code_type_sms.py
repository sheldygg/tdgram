from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeSms(BaseType):
    """
    A digit-only authentication code is delivered via an SMS message to the specified phone number; non-official applications may not receive this type of code
    """

    __type__: Literal["authenticationCodeTypeSms"] = "authenticationCodeTypeSms"

    length: int
    """Length of the code"""
