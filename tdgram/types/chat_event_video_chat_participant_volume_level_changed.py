from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class ChatEventVideoChatParticipantVolumeLevelChanged(BaseType):
    """
    A video chat participant volume level was changed
    """

    __type__: Literal["chatEventVideoChatParticipantVolumeLevelChanged"] = (
        "chatEventVideoChatParticipantVolumeLevelChanged"
    )

    participant_id: MessageSender
    """Identifier of the affected group call participant"""
    volume_level: int
    """New value of volume_level; 1-20000 in hundreds of percents"""
