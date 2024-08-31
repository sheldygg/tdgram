from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateWaitPassword(BaseType):
    """
    The user has been authorized, but needs to enter a 2-step verification password to start using the application.
    """

    __type__: Literal["authorizationStateWaitPassword"] = "authorizationStateWaitPassword"

    password_hint: str | None = None
    """Hint for the password; may be empty"""
    has_recovery_email_address: bool
    """True, if a recovery email address has been set up"""
    has_passport_data: bool
    """True, if some Telegram Passport elements were saved"""
    recovery_email_address_pattern: str
    """Pattern of the email address to which the recovery email was sent; empty until a recovery email has been sent"""
