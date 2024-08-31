from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendAuthenticationFirebaseSms(BaseMethod):
    """
    Sends Firebase Authentication SMS to the phone number of the user. Works only when the current authorization state is authorizationStateWaitCode and the server returned code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos
    """

    __type__: Literal["sendAuthenticationFirebaseSms"] = "sendAuthenticationFirebaseSms"
    __returning_type__ = Ok

    token: str
    """Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application"""
