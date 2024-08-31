from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallDiscardReasonDisconnected(BaseType):
    """
    The call was ended during the conversation because the users were disconnected
    """

    __type__: Literal["callDiscardReasonDisconnected"] = "callDiscardReasonDisconnected"
