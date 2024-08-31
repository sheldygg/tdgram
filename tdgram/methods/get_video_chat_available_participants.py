from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSenders
from .base import BaseMethod


@dataclass(kw_only=True)
class GetVideoChatAvailableParticipants(BaseMethod):
    """
    Returns the list of participant identifiers, on whose behalf a video chat in the chat can be joined
    """

    __type__: Literal["getVideoChatAvailableParticipants"] = "getVideoChatAvailableParticipants"
    __returning_type__ = MessageSenders

    chat_id: int
    """Chat identifier"""
