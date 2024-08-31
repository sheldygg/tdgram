from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypePublicChat(BaseType):
    """
    The link is a link to a chat by its username. Call searchPublicChat with the given chat username to process the link
    """

    __type__: Literal["internalLinkTypePublicChat"] = "internalLinkTypePublicChat"

    chat_username: str
    """Username of the chat"""
    draft_text: str
    """Draft text for message to send in the chat"""
    open_profile: bool
    """True, if chat profile information screen must be opened; otherwise, the chat itself must be opened"""
