from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallProblemDropped(BaseType):
    """
    The call ended unexpectedly
    """

    __type__: Literal["callProblemDropped"] = "callProblemDropped"
