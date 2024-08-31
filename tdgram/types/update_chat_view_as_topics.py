from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatViewAsTopics(BaseType):
    """
    A chat default appearance has changed
    """

    __type__: Literal["updateChatViewAsTopics"] = "updateChatViewAsTopics"

    chat_id: int
    """Chat identifier"""
    view_as_topics: bool
    """New value of view_as_topics"""
