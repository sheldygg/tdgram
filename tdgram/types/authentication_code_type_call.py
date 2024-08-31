from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeCall(BaseType):
    """
    A digit-only authentication code is delivered via a phone call to the specified phone number
    """

    __type__: Literal["authenticationCodeTypeCall"] = "authenticationCodeTypeCall"

    length: int
    """Length of the code"""
