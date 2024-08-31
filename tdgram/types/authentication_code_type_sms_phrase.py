from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeSmsPhrase(BaseType):
    """
    An authentication code is a phrase from multiple words delivered via an SMS message to the specified phone number; non-official applications may not receive this type of code
    """

    __type__: Literal["authenticationCodeTypeSmsPhrase"] = "authenticationCodeTypeSmsPhrase"

    first_word: str
    """The first word of the phrase if known"""
