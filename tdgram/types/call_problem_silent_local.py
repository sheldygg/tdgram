from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallProblemSilentLocal(BaseType):
    """
    The user couldn't hear the other side
    """

    __type__: Literal["callProblemSilentLocal"] = "callProblemSilentLocal"
