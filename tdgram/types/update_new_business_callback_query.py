from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessMessage, CallbackQueryPayload


@dataclass(kw_only=True)
class UpdateNewBusinessCallbackQuery(BaseType):
    """
    A new incoming callback query from a business message; for bots only
    """

    __type__: Literal["updateNewBusinessCallbackQuery"] = "updateNewBusinessCallbackQuery"

    id: int
    """Unique query identifier"""
    sender_user_id: int
    """Identifier of the user who sent the query"""
    connection_id: str
    """Unique identifier of the business connection"""
    message: BusinessMessage
    """The message from the business account from which the query originated"""
    chat_instance: int
    """An identifier uniquely corresponding to the chat a message was sent to"""
    payload: CallbackQueryPayload
    """Query payload"""
