from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Text
from .base import BaseMethod


@dataclass(kw_only=True)
class JoinGroupCall(BaseMethod):
    """
    Joins an active group call. Returns join response payload for tgcalls
    """

    __type__: Literal["joinGroupCall"] = "joinGroupCall"
    __returning_type__ = Text

    group_call_id: int
    """Group call identifier"""
    participant_id: MessageSender | None = None
    """Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only"""
    audio_source_id: int
    """Caller audio channel synchronization source identifier; received from tgcalls"""
    payload: str
    """Group call join payload; received from tgcalls"""
    is_muted: bool
    """Pass true to join the call with muted microphone"""
    is_my_video_enabled: bool
    """Pass true if the user's video is enabled"""
    invite_hash: str | None = None
    """If non-empty, invite hash to be used to join the group call without being muted by administrators"""
