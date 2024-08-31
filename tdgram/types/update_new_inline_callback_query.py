from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CallbackQueryPayload


@dataclass(kw_only=True)
class UpdateNewInlineCallbackQuery(BaseType):
    """
    A new incoming callback query from a message sent via a bot; for bots only
    """

    __type__: Literal["updateNewInlineCallbackQuery"] = "updateNewInlineCallbackQuery"

    id: int
    """Unique query identifier"""
    sender_user_id: int
    """Identifier of the user who sent the query"""
    inline_message_id: str
    """Identifier of the inline message from which the query originated"""
    chat_instance: int
    """An identifier uniquely corresponding to the chat a message was sent to"""
    payload: CallbackQueryPayload
    """Query payload"""
