from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetGroupCallParticipantVolumeLevel(BaseMethod):
    """
    Changes volume level of a participant of an active group call. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level
    """

    __type__: Literal["setGroupCallParticipantVolumeLevel"] = "setGroupCallParticipantVolumeLevel"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    participant_id: MessageSender
    """Participant identifier"""
    volume_level: int
    """New participant's volume level; 1-20000 in hundreds of percents"""
