from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class StartGroupCallScreenSharing(BaseMethod):
    """
    Starts screen sharing in a joined group call. Returns join response payload for tgcalls
    """

    __type__: Literal["startGroupCallScreenSharing"] = "startGroupCallScreenSharing"
    __returning_type__ = Text

    group_call_id: int
    """Group call identifier"""
    audio_source_id: int
    """Screen sharing audio channel synchronization source identifier; received from tgcalls"""
    payload: str
    """Group call join payload; received from tgcalls"""
