from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender, PushMessageContent


@dataclass(kw_only=True)
class NotificationTypeNewPushMessage(BaseType):
    """
    New message was received through a push notification
    """

    __type__: Literal["notificationTypeNewPushMessage"] = "notificationTypeNewPushMessage"

    message_id: int
    """The message identifier. The message will not be available in the chat history, but the identifier can be used in viewMessages, or as a message to be replied in the same chat"""
    sender_id: MessageSender
    """Identifier of the sender of the message. Corresponding user or chat may be inaccessible"""
    sender_name: str
    """Name of the sender"""
    is_outgoing: bool
    """True, if the message is outgoing"""
    content: PushMessageContent
    """Push message content"""
