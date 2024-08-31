from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputTextQuote, Messages
from .base import BaseMethod


@dataclass(kw_only=True)
class ResendMessages(BaseMethod):
    """
    Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed.
    """

    __type__: Literal["resendMessages"] = "resendMessages"
    __returning_type__ = Messages

    chat_id: int
    """Identifier of the chat to send messages"""
    message_ids: list[int]
    """Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order"""
    quote: InputTextQuote | None = None
    """New manually chosen quote from the message to be replied; pass null if none. Ignored if more than one message is re-sent, or if messageSendingStateFailed.need_another_reply_quote == false"""
