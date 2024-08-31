from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleGroupCallParticipantIsHandRaised(BaseMethod):
    """
    Toggles whether a group call participant hand is rased
    """

    __type__: Literal["toggleGroupCallParticipantIsHandRaised"] = (
        "toggleGroupCallParticipantIsHandRaised"
    )
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    participant_id: MessageSender
    """Participant identifier"""
    is_hand_raised: bool
    """Pass true if the user's hand needs to be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand"""
