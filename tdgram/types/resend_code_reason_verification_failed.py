from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ResendCodeReasonVerificationFailed(BaseType):
    """
    The code is re-sent, because device verification has failed
    """

    __type__: Literal["resendCodeReasonVerificationFailed"] = "resendCodeReasonVerificationFailed"

    error_message: str
    """Cause of the verification failure, for example, PLAY_SERVICES_NOT_AVAILABLE, APNS_RECEIVE_TIMEOUT, or APNS_INIT_FAILED"""
