from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchChatAffiliateProgram(BaseMethod):
    """
    Searches a chat with an affiliate program. Returns the chat if found and the program is active
    """

    __type__: Literal["searchChatAffiliateProgram"] = "searchChatAffiliateProgram"
    __returning_type__ = Chat

    username: str
    """Username of the chat"""
    referrer: str
    """The referrer from an internalLinkTypeChatAffiliateProgram link"""
