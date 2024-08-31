from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Error, Message


@dataclass(kw_only=True)
class UpdateMessageSendFailed(BaseType):
    """
    A message failed to send. Be aware that some messages being sent can be irrecoverably deleted, in which case updateDeleteMessages will be received instead of this update
    """

    __type__: Literal["updateMessageSendFailed"] = "updateMessageSendFailed"

    message: Message
    """The failed to send message"""
    old_message_id: int
    """The previous temporary message identifier"""
    error: Error
    """The cause of the message sending failure"""
