from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeFlashCall(BaseType):
    """
    An authentication code is delivered by an immediately canceled call to the specified phone number. The phone number that calls is the code that must be entered automatically
    """

    __type__: Literal["authenticationCodeTypeFlashCall"] = "authenticationCodeTypeFlashCall"

    pattern: str
    """Pattern of the phone number from which the call will be made"""
