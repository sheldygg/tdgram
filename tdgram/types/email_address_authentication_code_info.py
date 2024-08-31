from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmailAddressAuthenticationCodeInfo(BaseType):
    """
    Information about the email address authentication code that was sent
    """

    __type__: Literal["emailAddressAuthenticationCodeInfo"] = "emailAddressAuthenticationCodeInfo"

    email_address_pattern: str
    """Pattern of the email address to which an authentication code was sent"""
    length: int
    """Length of the code; 0 if unknown"""
