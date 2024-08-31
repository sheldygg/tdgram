from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatsToSendStories(BaseMethod):
    """
    Returns supergroup and channel chats in which the current user has the right to post stories. The chats must be rechecked with canSendStory before actually trying to post a story there
    """

    __type__: Literal["getChatsToSendStories"] = "getChatsToSendStories"
    __returning_type__ = Chats
