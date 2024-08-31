from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteChatReplyMarkup(BaseMethod):
    """
    Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a replyMarkupForceReply reply markup has been used. An updateChatReplyMarkup update will be sent if the reply markup is changed
    """

    __type__: Literal["deleteChatReplyMarkup"] = "deleteChatReplyMarkup"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_id: int
    """The message identifier of the used keyboard"""
