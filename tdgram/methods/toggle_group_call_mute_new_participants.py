from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleGroupCallMuteNewParticipants(BaseMethod):
    """
    Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_toggle_mute_new_participants group call flag
    """

    __type__: Literal["toggleGroupCallMuteNewParticipants"] = "toggleGroupCallMuteNewParticipants"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    mute_new_participants: bool
    """New value of the mute_new_participants setting"""
