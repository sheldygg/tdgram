from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class ChatEventVideoChatParticipantIsMutedToggled(BaseType):
    """
    A video chat participant was muted or unmuted
    """

    __type__: Literal["chatEventVideoChatParticipantIsMutedToggled"] = (
        "chatEventVideoChatParticipantIsMutedToggled"
    )

    participant_id: MessageSender
    """Identifier of the affected group call participant"""
    is_muted: bool
    """New value of is_muted"""
