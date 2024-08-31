from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateWaitEmailAddress(BaseType):
    """
    TDLib needs the user's email address to authorize. Call setAuthenticationEmailAddress to provide the email address, or directly call checkAuthenticationEmailCode with Apple ID/Google ID token if allowed
    """

    __type__: Literal["authorizationStateWaitEmailAddress"] = "authorizationStateWaitEmailAddress"

    allow_apple_id: bool
    """True, if authorization through Apple ID is allowed"""
    allow_google_id: bool
    """True, if authorization through Google ID is allowed"""
