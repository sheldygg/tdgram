from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CallbackQueryAnswer, CallbackQueryPayload
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCallbackQueryAnswer(BaseMethod):
    """
    Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
    """

    __type__: Literal["getCallbackQueryAnswer"] = "getCallbackQueryAnswer"
    __returning_type__ = CallbackQueryAnswer

    chat_id: int
    """Identifier of the chat with the message"""
    message_id: int
    """Identifier of the message from which the query originated. The message must not be scheduled"""
    payload: CallbackQueryPayload
    """Query payload"""
