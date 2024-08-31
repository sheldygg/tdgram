from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EmailAddressAuthenticationCodeInfo, EmailAddressResetState


@dataclass(kw_only=True)
class AuthorizationStateWaitEmailCode(BaseType):
    """
    TDLib needs the user's authentication code sent to an email address to authorize. Call checkAuthenticationEmailCode to provide the code
    """

    __type__: Literal["authorizationStateWaitEmailCode"] = "authorizationStateWaitEmailCode"

    allow_apple_id: bool
    """True, if authorization through Apple ID is allowed"""
    allow_google_id: bool
    """True, if authorization through Google ID is allowed"""
    code_info: EmailAddressAuthenticationCodeInfo
    """Information about the sent authentication code"""
    email_address_reset_state: EmailAddressResetState | None = None
    """Reset state of the email address; may be null if the email address can't be reset"""
