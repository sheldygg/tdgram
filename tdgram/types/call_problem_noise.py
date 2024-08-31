from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallProblemNoise(BaseType):
    """
    The user heard background noise
    """

    __type__: Literal["callProblemNoise"] = "callProblemNoise"
