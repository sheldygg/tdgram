from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallProblemEcho(BaseType):
    """
    The user heard their own voice
    """

    __type__: Literal["callProblemEcho"] = "callProblemEcho"
