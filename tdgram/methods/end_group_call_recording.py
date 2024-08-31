from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EndGroupCallRecording(BaseMethod):
    """
    Ends recording of an active group call. Requires groupCall.can_be_managed group call flag
    """

    __type__: Literal["endGroupCallRecording"] = "endGroupCallRecording"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
