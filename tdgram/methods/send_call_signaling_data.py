from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendCallSignalingData(BaseMethod):
    """
    Sends call signaling data
    """

    __type__: Literal["sendCallSignalingData"] = "sendCallSignalingData"
    __returning_type__ = Ok

    call_id: int
    """Call identifier"""
    data: bytes
    """The data"""
