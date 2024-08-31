from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendPhoneNumberFirebaseSms(BaseMethod):
    """
    Sends Firebase Authentication SMS to the specified phone number. Works only when received a code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos
    """

    __type__: Literal["sendPhoneNumberFirebaseSms"] = "sendPhoneNumberFirebaseSms"
    __returning_type__ = Ok

    token: str
    """Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application"""
