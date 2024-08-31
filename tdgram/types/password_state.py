from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EmailAddressAuthenticationCodeInfo


@dataclass(kw_only=True)
class PasswordState(BaseType):
    """
    Represents the current state of 2-step verification
    """

    __type__: Literal["passwordState"] = "passwordState"

    has_password: bool
    """True, if a 2-step verification password is set"""
    password_hint: str | None = None
    """Hint for the password; may be empty"""
    has_recovery_email_address: bool
    """True, if a recovery email is set"""
    has_passport_data: bool
    """True, if some Telegram Passport elements were saved"""
    recovery_email_address_code_info: EmailAddressAuthenticationCodeInfo | None = None
    """Information about the recovery email address to which the confirmation email was sent; may be null"""
    login_email_address_pattern: str
    """Pattern of the email address set up for logging in"""
    pending_reset_date: int
    """If not 0, point in time (Unix timestamp) after which the 2-step verification password can be reset immediately using resetPassword"""
