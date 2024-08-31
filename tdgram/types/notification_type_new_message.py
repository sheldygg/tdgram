from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class NotificationTypeNewMessage(BaseType):
    """
    New message was received
    """

    __type__: Literal["notificationTypeNewMessage"] = "notificationTypeNewMessage"

    message: Message
    """The message"""
    show_preview: bool
    """True, if message content must be displayed in notifications"""
