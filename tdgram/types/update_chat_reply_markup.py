from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatReplyMarkup(BaseType):
    """
    The default chat reply markup was changed. Can occur because new messages with reply markup were received or because an old reply markup was hidden by the user
    """

    __type__: Literal["updateChatReplyMarkup"] = "updateChatReplyMarkup"

    chat_id: int
    """Chat identifier"""
    reply_markup_message_id: int
    """Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat"""
