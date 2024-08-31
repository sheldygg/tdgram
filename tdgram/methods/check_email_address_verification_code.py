from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckEmailAddressVerificationCode(BaseMethod):
    """
    Checks the email address verification code for Telegram Passport
    """

    __type__: Literal["checkEmailAddressVerificationCode"] = "checkEmailAddressVerificationCode"
    __returning_type__ = Ok

    code: str
    """Verification code to check"""
