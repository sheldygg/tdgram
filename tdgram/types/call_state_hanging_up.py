from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallStateHangingUp(BaseType):
    """
    The call is hanging up after discardCall has been called
    """

    __type__: Literal["callStateHangingUp"] = "callStateHangingUp"
