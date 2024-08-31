from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallProblemDistortedVideo(BaseType):
    """
    The video was distorted
    """

    __type__: Literal["callProblemDistortedVideo"] = "callProblemDistortedVideo"
