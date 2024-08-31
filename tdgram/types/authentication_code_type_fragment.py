from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthenticationCodeTypeFragment(BaseType):
    """
    A digit-only authentication code is delivered to https://fragment.com. The user must be logged in there via a wallet owning the phone number's NFT
    """

    __type__: Literal["authenticationCodeTypeFragment"] = "authenticationCodeTypeFragment"

    url: str
    """URL to open to receive the code"""
    length: int
    """Length of the code"""
