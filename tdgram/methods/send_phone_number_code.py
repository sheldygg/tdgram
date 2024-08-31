from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AuthenticationCodeInfo, PhoneNumberAuthenticationSettings, PhoneNumberCodeType
from .base import BaseMethod


@dataclass(kw_only=True)
class SendPhoneNumberCode(BaseMethod):
    """
    Sends a code to the specified phone number. Aborts previous phone number verification if there was one. On success, returns information about the sent code
    """

    __type__: Literal["sendPhoneNumberCode"] = "sendPhoneNumberCode"
    __returning_type__ = AuthenticationCodeInfo

    phone_number: str
    """The phone number, in international format"""
    settings: PhoneNumberAuthenticationSettings | None = None
    """Settings for the authentication of the user's phone number; pass null to use default settings"""
    type: PhoneNumberCodeType
    """Type of the request for which the code is sent"""
