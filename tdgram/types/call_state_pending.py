from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallStatePending(BaseType):
    """
    The call is pending, waiting to be accepted by a user
    """

    __type__: Literal["callStatePending"] = "callStatePending"

    is_created: bool
    """True, if the call has already been created by the server"""
    is_received: bool
    """True, if the call has already been received by the other party"""
