from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteChat(BaseMethod):
    """
    Deletes a chat along with all messages in the corresponding chat for all chat members. For group chats this will release the usernames and remove all members.
    """

    __type__: Literal["deleteChat"] = "deleteChat"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
