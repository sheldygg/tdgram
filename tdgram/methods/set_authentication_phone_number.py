from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, PhoneNumberAuthenticationSettings
from .base import BaseMethod


@dataclass(kw_only=True)
class SetAuthenticationPhoneNumber(BaseMethod):
    """
    Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber,
    """

    __type__: Literal["setAuthenticationPhoneNumber"] = "setAuthenticationPhoneNumber"
    __returning_type__ = Ok

    phone_number: str
    """The phone number of the user, in international format"""
    settings: PhoneNumberAuthenticationSettings | None = None
    """Settings for the authentication of the user's phone number; pass null to use default settings"""
