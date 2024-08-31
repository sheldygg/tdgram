from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class UpdateMessageSendSucceeded(BaseType):
    """
    A message has been successfully sent
    """

    __type__: Literal["updateMessageSendSucceeded"] = "updateMessageSendSucceeded"

    message: Message
    """The sent message. Usually only the message identifier, date, and content are changed, but almost all other fields can also change"""
    old_message_id: int
    """The previous temporary message identifier"""
