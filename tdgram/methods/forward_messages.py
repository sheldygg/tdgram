from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Messages, MessageSendOptions
from .base import BaseMethod


@dataclass(kw_only=True)
class ForwardMessages(BaseMethod):
    """
    Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message
    """

    __type__: Literal["forwardMessages"] = "forwardMessages"
    __returning_type__ = Messages

    chat_id: int
    """Identifier of the chat to which to forward messages"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the message will be sent; for forum threads only"""
    from_chat_id: int
    """Identifier of the chat from which to forward messages"""
    message_ids: list[int]
    """Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously. A message can be forwarded only if messageProperties.can_be_forwarded"""
    options: MessageSendOptions | None = None
    """Options to be used to send the messages; pass null to use default options"""
    send_copy: bool
    """Pass true to copy content of the messages without reference to the original sender. Always true if the messages are forwarded to a secret chat or are local."""
    remove_caption: bool
    """Pass true to remove media captions of message copies. Ignored if send_copy is false"""
