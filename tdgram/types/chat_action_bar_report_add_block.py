from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionBarReportAddBlock(BaseType):
    """
    The chat is a private or secret chat, which can be reported using the method reportChat, or the other user can be blocked using the method setMessageSenderBlockList,
    """

    __type__: Literal["chatActionBarReportAddBlock"] = "chatActionBarReportAddBlock"

    can_unarchive: bool
    """If true, the chat was automatically archived and can be moved back to the main chat list using addChatToList simultaneously with setting chat notification settings to default using setChatNotificationSettings"""
