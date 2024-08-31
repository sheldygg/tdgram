from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CallbackQueryPayload


@dataclass(kw_only=True)
class UpdateNewCallbackQuery(BaseType):
    """
    A new incoming callback query; for bots only
    """

    __type__: Literal["updateNewCallbackQuery"] = "updateNewCallbackQuery"

    id: int
    """Unique query identifier"""
    sender_user_id: int
    """Identifier of the user who sent the query"""
    chat_id: int
    """Identifier of the chat where the query was sent"""
    message_id: int
    """Identifier of the message from which the query originated"""
    chat_instance: int
    """Identifier that uniquely corresponds to the chat to which the message was sent"""
    payload: CallbackQueryPayload
    """Query payload"""
