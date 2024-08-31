from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputTextQuote


@dataclass(kw_only=True)
class InputMessageReplyToExternalMessage(BaseType):
    """
    Describes a message to be replied that is from a different chat or a forum topic; not supported in secret chats
    """

    __type__: Literal["inputMessageReplyToExternalMessage"] = "inputMessageReplyToExternalMessage"

    chat_id: int
    """The identifier of the chat to which the message to be replied belongs"""
    message_id: int
    """The identifier of the message to be replied in the specified chat. A message can be replied in another chat or forum topic only if messageProperties.can_be_replied_in_another_chat"""
    quote: InputTextQuote | None = None
    """Quote from the message to be replied; pass null if none"""
