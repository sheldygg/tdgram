from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallDiscardReasonAllowGroupCall(BaseType):
    """
    The call was ended because it has been used successfully to transfer private encryption key for the associated group call
    """

    __type__: Literal["callDiscardReasonAllowGroupCall"] = "callDiscardReasonAllowGroupCall"

    encrypted_group_call_key: bytes
    """Encrypted using the call private key encryption key for the associated group call"""
