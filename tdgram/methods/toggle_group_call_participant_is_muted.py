from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleGroupCallParticipantIsMuted(BaseMethod):
    """
    Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves
    """

    __type__: Literal["toggleGroupCallParticipantIsMuted"] = "toggleGroupCallParticipantIsMuted"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    participant_id: MessageSender
    """Participant identifier"""
    is_muted: bool
    """Pass true to mute the user; pass false to unmute them"""
