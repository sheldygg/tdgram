from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetApplicationVerificationToken(BaseMethod):
    """
    Application verification has been completed. Can be called before authorization
    """

    __type__: Literal["setApplicationVerificationToken"] = "setApplicationVerificationToken"
    __returning_type__ = Ok

    verification_id: int
    """Unique identifier for the verification process as received from updateApplicationVerificationRequired"""
    token: str
    """Play Integrity API token for the Android application, or secret from push notification for the iOS application;"""
