from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventVideoChatMuteNewParticipantsToggled(BaseType):
    """
    The mute_new_participants setting of a video chat was toggled
    """

    __type__: Literal["chatEventVideoChatMuteNewParticipantsToggled"] = (
        "chatEventVideoChatMuteNewParticipantsToggled"
    )

    mute_new_participants: bool
    """New value of the mute_new_participants setting"""
