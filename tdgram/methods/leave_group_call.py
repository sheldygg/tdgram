from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class LeaveGroupCall(BaseMethod):
    """
    Leaves a group call
    """

    __type__: Literal["leaveGroupCall"] = "leaveGroupCall"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
