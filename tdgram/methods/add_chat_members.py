from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FailedToAddMembers
from .base import BaseMethod


@dataclass(kw_only=True)
class AddChatMembers(BaseMethod):
    """
    Adds multiple new members to a chat; requires can_invite_users member right. Currently, this method is only available for supergroups and channels.
    """

    __type__: Literal["addChatMembers"] = "addChatMembers"
    __returning_type__ = FailedToAddMembers

    chat_id: int
    """Chat identifier"""
    user_ids: list[int]
    """Identifiers of the users to be added to the chat. The maximum number of added users is 20 for supergroups and 100 for channels"""
