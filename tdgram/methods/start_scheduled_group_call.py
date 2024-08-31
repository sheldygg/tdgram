from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class StartScheduledGroupCall(BaseMethod):
    """
    Starts a scheduled group call
    """

    __type__: Literal["startScheduledGroupCall"] = "startScheduledGroupCall"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
