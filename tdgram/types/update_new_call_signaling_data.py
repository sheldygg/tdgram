from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateNewCallSignalingData(BaseType):
    """
    New call signaling data arrived
    """

    __type__: Literal["updateNewCallSignalingData"] = "updateNewCallSignalingData"

    call_id: int
    """The call identifier"""
    data: bytes
    """The data"""
