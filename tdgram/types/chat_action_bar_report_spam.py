from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionBarReportSpam(BaseType):
    """
    The chat can be reported as spam using the method reportChat with the reason reportReasonSpam. If the chat is a private chat with a user with an emoji status, then a notice about emoji status usage must be shown
    """

    __type__: Literal["chatActionBarReportSpam"] = "chatActionBarReportSpam"

    can_unarchive: bool
    """If true, the chat was automatically archived and can be moved back to the main chat list using addChatToList simultaneously with setting chat notification settings to default using setChatNotificationSettings"""
