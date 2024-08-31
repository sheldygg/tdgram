from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleChatViewAsTopics(BaseMethod):
    """
    Changes the view_as_topics setting of a forum chat or Saved Messages
    """

    __type__: Literal["toggleChatViewAsTopics"] = "toggleChatViewAsTopics"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    view_as_topics: bool
    """New value of view_as_topics"""
