from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageInviteVideoChatParticipants(BaseType):
    """
    A message with information about an invitation to a video chat
    """

    __type__: Literal["messageInviteVideoChatParticipants"] = "messageInviteVideoChatParticipants"

    group_call_id: int
    """Identifier of the video chat. The video chat can be received through the method getGroupCall"""
    user_ids: list[int]
    """Invited user identifiers"""
