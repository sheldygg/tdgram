from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import SponsoredMessages
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatSponsoredMessages(BaseMethod):
    """
    Returns sponsored messages to be shown in a chat; for channel chats and chats with bots only
    """

    __type__: Literal["getChatSponsoredMessages"] = "getChatSponsoredMessages"
    __returning_type__ = SponsoredMessages

    chat_id: int
    """Identifier of the chat"""
