from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeSmsWord(BaseType):
    """
    An authentication code is a word delivered via an SMS message to the specified phone number; non-official applications may not receive this type of code
    """

    __type__: Literal["authenticationCodeTypeSmsWord"] = "authenticationCodeTypeSmsWord"

    first_letter: str
    """The first letters of the word if known"""
