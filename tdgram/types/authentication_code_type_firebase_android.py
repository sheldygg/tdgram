from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FirebaseDeviceVerificationParameters


@dataclass(kw_only=True)
class AuthenticationCodeTypeFirebaseAndroid(BaseType):
    """
    A digit-only authentication code is delivered via Firebase Authentication to the official Android application
    """

    __type__: Literal["authenticationCodeTypeFirebaseAndroid"] = (
        "authenticationCodeTypeFirebaseAndroid"
    )

    device_verification_parameters: FirebaseDeviceVerificationParameters
    """Parameters to be used for device verification"""
    length: int
    """Length of the code"""
