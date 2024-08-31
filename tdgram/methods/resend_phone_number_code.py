from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AuthenticationCodeInfo, ResendCodeReason
from .base import BaseMethod


@dataclass(kw_only=True)
class ResendPhoneNumberCode(BaseMethod):
    """
    Resends the authentication code sent to a phone number. Works only if the previously received authenticationCodeInfo next_code_type was not null and the server-specified timeout has passed
    """

    __type__: Literal["resendPhoneNumberCode"] = "resendPhoneNumberCode"
    __returning_type__ = AuthenticationCodeInfo

    reason: ResendCodeReason | None = None
    """Reason of code resending; pass null if unknown"""
