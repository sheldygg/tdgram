from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmailAddressAuthentication, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckAuthenticationEmailCode(BaseMethod):
    """
    Checks the authentication of an email address. Works only when the current authorization state is authorizationStateWaitEmailCode
    """

    __type__: Literal["checkAuthenticationEmailCode"] = "checkAuthenticationEmailCode"
    __returning_type__ = Ok

    code: EmailAddressAuthentication
    """Email address authentication to check"""
