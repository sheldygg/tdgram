from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleGroupCallScreenSharingIsPaused(BaseMethod):
    """
    Pauses or unpauses screen sharing in a joined group call
    """

    __type__: Literal["toggleGroupCallScreenSharingIsPaused"] = (
        "toggleGroupCallScreenSharingIsPaused"
    )
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    is_paused: bool
    """Pass true to pause screen sharing; pass false to unpause it"""
