from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmailAddressAuthenticationCodeInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class SendEmailAddressVerificationCode(BaseMethod):
    """
    Sends a code to verify an email address to be added to a user's Telegram Passport
    """

    __type__: Literal["sendEmailAddressVerificationCode"] = "sendEmailAddressVerificationCode"
    __returning_type__ = EmailAddressAuthenticationCodeInfo

    email_address: str
    """Email address"""
