from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Messages
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageThreadHistory(BaseMethod):
    """
    Returns messages in a message thread of a message. Can be used only if messageProperties.can_get_message_thread == true. Message thread of a channel message is in the channel's linked supergroup.
    """

    __type__: Literal["getMessageThreadHistory"] = "getMessageThreadHistory"
    __returning_type__ = Messages

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier, which thread history needs to be returned"""
    from_message_id: int
    """Identifier of the message starting from which history must be fetched; use 0 to get results from the last message"""
    offset: int
    """Specify 0 to get results from exactly the message from_message_id or a negative offset up to 99 to get additionally some newer messages"""
    limit: int
    """The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset."""
