from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallDiscardReasonHungUp(BaseType):
    """
    The call was ended because one of the parties hung up
    """

    __type__: Literal["callDiscardReasonHungUp"] = "callDiscardReasonHungUp"
