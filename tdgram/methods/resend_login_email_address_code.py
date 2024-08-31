from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmailAddressAuthenticationCodeInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class ResendLoginEmailAddressCode(BaseMethod):
    """
    Resends the login email address verification code
    """

    __type__: Literal["resendLoginEmailAddressCode"] = "resendLoginEmailAddressCode"
    __returning_type__ = EmailAddressAuthenticationCodeInfo
