from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmailAddressResetStatePending(BaseType):
    """
    Email address reset has already been requested. Call resetAuthenticationEmailAddress to check whether immediate reset is possible
    """

    __type__: Literal["emailAddressResetStatePending"] = "emailAddressResetStatePending"

    reset_in: int
    """Left time before the email address will be reset, in seconds. updateAuthorizationState is not sent when this field changes"""
