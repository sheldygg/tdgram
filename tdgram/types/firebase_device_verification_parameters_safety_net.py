from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FirebaseDeviceVerificationParametersSafetyNet(BaseType):
    """
    Device verification must be performed with the SafetyNet Attestation API
    """

    __type__: Literal["firebaseDeviceVerificationParametersSafetyNet"] = (
        "firebaseDeviceVerificationParametersSafetyNet"
    )

    nonce: bytes
    """Nonce to pass to the SafetyNet Attestation API"""
