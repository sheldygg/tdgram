from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallDiscardReasonMissed(BaseType):
    """
    The call was ended before the conversation started. It was canceled by the caller or missed by the other party
    """

    __type__: Literal["callDiscardReasonMissed"] = "callDiscardReasonMissed"
