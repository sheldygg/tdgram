from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallProblemDistortedSpeech(BaseType):
    """
    The speech was distorted
    """

    __type__: Literal["callProblemDistortedSpeech"] = "callProblemDistortedSpeech"
