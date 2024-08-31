from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmailAddressAuthenticationGoogleId(BaseType):
    """
    An authentication token received through Google ID
    """

    __type__: Literal["emailAddressAuthenticationGoogleId"] = "emailAddressAuthenticationGoogleId"

    token: str
    """The token"""
