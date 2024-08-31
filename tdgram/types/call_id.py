from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallId(BaseType):
    """
    Contains the call identifier
    """

    __type__: Literal["callId"] = "callId"

    id: int
    """Call identifier"""
