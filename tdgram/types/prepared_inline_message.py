from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InlineQueryResult, TargetChatTypes


@dataclass(kw_only=True)
class PreparedInlineMessage(BaseType):
    """
    Represents a ready to send inline message. Use sendInlineQueryResultMessage to send the message
    """

    __type__: Literal["preparedInlineMessage"] = "preparedInlineMessage"

    inline_query_id: int
    """Unique identifier of the inline query to pass to sendInlineQueryResultMessage"""
    result: InlineQueryResult
    """Resulted inline message of the query"""
    chat_types: TargetChatTypes
    """Types of the chats to which the message can be sent"""
