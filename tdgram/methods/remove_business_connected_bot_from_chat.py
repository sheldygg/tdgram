from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveBusinessConnectedBotFromChat(BaseMethod):
    """
    Removes the connected business bot from a specific chat by adding the chat to businessRecipients.excluded_chat_ids
    """

    __type__: Literal["removeBusinessConnectedBotFromChat"] = "removeBusinessConnectedBotFromChat"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
