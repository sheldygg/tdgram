from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateApplicationVerificationRequired(BaseType):
    """
    A request can't be completed unless application verification is performed; for official mobile applications only.
    """

    __type__: Literal["updateApplicationVerificationRequired"] = (
        "updateApplicationVerificationRequired"
    )

    verification_id: int
    """Unique identifier for the verification process"""
    nonce: str
    """Unique base64url-encoded nonce for the classic Play Integrity verification (https://developer.android.com/google/play/integrity/classic) for Android,"""
    cloud_project_number: int
    """Cloud project number to pass to the Play Integrity API on Android"""
