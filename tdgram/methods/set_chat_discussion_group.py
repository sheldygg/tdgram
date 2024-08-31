from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatDiscussionGroup(BaseMethod):
    """
    Changes the discussion group of a channel chat; requires can_change_info administrator right in the channel if it is specified
    """

    __type__: Literal["setChatDiscussionGroup"] = "setChatDiscussionGroup"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the channel chat. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat (requires can_pin_messages member right in the supergroup)"""
    discussion_chat_id: int
    """Identifier of a new channel's discussion group. Use 0 to remove the discussion group. Use the method getSuitableDiscussionChats to find all suitable groups."""
