from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetVideoChatDefaultParticipant(BaseMethod):
    """
    Changes default participant identifier, on whose behalf a video chat in the chat will be joined
    """

    __type__: Literal["setVideoChatDefaultParticipant"] = "setVideoChatDefaultParticipant"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    default_participant_id: MessageSender
    """Default group call participant identifier to join the video chats"""
