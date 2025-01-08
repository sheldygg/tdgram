from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputInlineQueryResult, PreparedInlineMessageId, TargetChatTypes
from .base import BaseMethod


@dataclass(kw_only=True)
class SavePreparedInlineMessage(BaseMethod):
    """
    Saves an inline message to be sent by the given user; for bots only
    """

    __type__: Literal["savePreparedInlineMessage"] = "savePreparedInlineMessage"
    __returning_type__ = PreparedInlineMessageId

    user_id: int
    """Identifier of the user"""
    result: InputInlineQueryResult
    """The description of the message"""
    chat_types: TargetChatTypes
    """Types of the chats to which the message can be sent"""
