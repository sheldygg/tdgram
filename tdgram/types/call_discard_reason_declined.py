from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallDiscardReasonDeclined(BaseType):
    """
    The call was ended before the conversation started. It was declined by the other party
    """

    __type__: Literal["callDiscardReasonDeclined"] = "callDiscardReasonDeclined"
