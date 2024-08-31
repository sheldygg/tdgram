from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetGroupCallParticipantIsSpeaking(BaseMethod):
    """
    Informs TDLib that speaking state of a participant of an active group has changed
    """

    __type__: Literal["setGroupCallParticipantIsSpeaking"] = "setGroupCallParticipantIsSpeaking"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    audio_source: int
    """Group call participant's synchronization audio source identifier, or 0 for the current user"""
    is_speaking: bool
    """Pass true if the user is speaking"""
