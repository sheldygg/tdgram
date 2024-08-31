from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatNotificationSettings, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetForumTopicNotificationSettings(BaseMethod):
    """
    Changes the notification settings of a forum topic
    """

    __type__: Literal["setForumTopicNotificationSettings"] = "setForumTopicNotificationSettings"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_thread_id: int
    """Message thread identifier of the forum topic"""
    notification_settings: ChatNotificationSettings
    """New notification settings for the forum topic. If the topic is muted for more than 366 days, it is considered to be muted forever"""
