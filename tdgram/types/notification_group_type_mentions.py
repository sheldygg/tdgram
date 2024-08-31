from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NotificationGroupTypeMentions(BaseType):
    """
    A group containing notifications of type notificationTypeNewMessage and notificationTypeNewPushMessage with unread mentions of the current user, replies to their messages, or a pinned message
    """

    __type__: Literal["notificationGroupTypeMentions"] = "notificationGroupTypeMentions"
