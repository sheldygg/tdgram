from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmailAddressAuthenticationCodeInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class ResendEmailAddressVerificationCode(BaseMethod):
    """
    Resends the code to verify an email address to be added to a user's Telegram Passport
    """

    __type__: Literal["resendEmailAddressVerificationCode"] = "resendEmailAddressVerificationCode"
    __returning_type__ = EmailAddressAuthenticationCodeInfo
