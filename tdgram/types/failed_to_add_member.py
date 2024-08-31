from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FailedToAddMember(BaseType):
    """
    Contains information about a user that has failed to be added to a chat
    """

    __type__: Literal["failedToAddMember"] = "failedToAddMember"

    user_id: int
    """User identifier"""
    premium_would_allow_invite: bool
    """True, if subscription to Telegram Premium would have allowed to add the user to the chat"""
    premium_required_to_send_messages: bool
    """True, if subscription to Telegram Premium is required to send the user chat invite link"""
