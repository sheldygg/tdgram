from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FirebaseDeviceVerificationParametersPlayIntegrity(BaseType):
    """
    Device verification must be performed with the classic Play Integrity verification (https://developer.android.com/google/play/integrity/classic)
    """

    __type__: Literal["firebaseDeviceVerificationParametersPlayIntegrity"] = (
        "firebaseDeviceVerificationParametersPlayIntegrity"
    )

    nonce: str
    """Base64url-encoded nonce to pass to the Play Integrity API"""
    cloud_project_number: int
    """Cloud project number to pass to the Play Integrity API"""
