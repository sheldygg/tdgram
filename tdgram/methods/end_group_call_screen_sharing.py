from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EndGroupCallScreenSharing(BaseMethod):
    """
    Ends screen sharing in a joined group call
    """

    __type__: Literal["endGroupCallScreenSharing"] = "endGroupCallScreenSharing"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
