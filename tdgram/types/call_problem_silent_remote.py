from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallProblemSilentRemote(BaseType):
    """
    The other side couldn't hear the user
    """

    __type__: Literal["callProblemSilentRemote"] = "callProblemSilentRemote"
