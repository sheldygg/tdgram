from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeVideoChat(BaseType):
    """
    The link is a link to a video chat. Call searchPublicChat with the given chat username, and then joinGroupCall with the given invite hash to process the link
    """

    __type__: Literal["internalLinkTypeVideoChat"] = "internalLinkTypeVideoChat"

    chat_username: str
    """Username of the chat with the video chat"""
    invite_hash: str | None = None
    """If non-empty, invite hash to be used to join the video chat without being muted by administrators"""
    is_live_stream: bool
    """True, if the video chat is expected to be a live stream in a channel or a broadcast group"""
