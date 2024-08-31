from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats, NotificationSettingsScope
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatNotificationSettingsExceptions(BaseMethod):
    """
    Returns the list of chats with non-default notification settings for new messages
    """

    __type__: Literal["getChatNotificationSettingsExceptions"] = (
        "getChatNotificationSettingsExceptions"
    )
    __returning_type__ = Chats

    scope: NotificationSettingsScope | None = None
    """If specified, only chats from the scope will be returned; pass null to return chats from all scopes"""
    compare_sound: bool
    """Pass true to include in the response chats with only non-default sound"""
