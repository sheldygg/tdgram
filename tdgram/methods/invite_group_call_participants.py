from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class InviteGroupCallParticipants(BaseMethod):
    """
    Invites users to an active group call. Sends a service message of type messageInviteVideoChatParticipants for video chats
    """

    __type__: Literal["inviteGroupCallParticipants"] = "inviteGroupCallParticipants"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    user_ids: list[int]
    """User identifiers. At most 10 users can be invited simultaneously"""
