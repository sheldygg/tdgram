from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmailAddressAuthenticationAppleId(BaseType):
    """
    An authentication token received through Apple ID
    """

    __type__: Literal["emailAddressAuthenticationAppleId"] = "emailAddressAuthenticationAppleId"

    token: str
    """The token"""
