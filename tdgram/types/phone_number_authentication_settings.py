from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FirebaseAuthenticationSettings


@dataclass(kw_only=True)
class PhoneNumberAuthenticationSettings(BaseType):
    """
    Contains settings for the authentication of the user's phone number
    """

    __type__: Literal["phoneNumberAuthenticationSettings"] = "phoneNumberAuthenticationSettings"

    allow_flash_call: bool
    """Pass true if the authentication code may be sent via a flash call to the specified phone number"""
    allow_missed_call: bool
    """Pass true if the authentication code may be sent via a missed call to the specified phone number"""
    is_current_phone_number: bool
    """Pass true if the authenticated phone number is used on the current device"""
    has_unknown_phone_number: bool
    """Pass true if there is a SIM card in the current device, but it is not possible to check whether phone number matches"""
    allow_sms_retriever_api: bool
    """For official applications only. True, if the application can use Android SMS Retriever API (requires Google Play Services >= 10.2) to automatically receive the authentication code from the SMS. See https://developers.google.com/identity/sms-retriever/ for more details"""
    firebase_authentication_settings: FirebaseAuthenticationSettings | None = None
    """For official Android and iOS applications only; pass null otherwise. Settings for Firebase Authentication"""
    authentication_tokens: list[str]
    """List of up to 20 authentication tokens, recently received in updateOption('authentication_token') in previously logged out sessions"""
