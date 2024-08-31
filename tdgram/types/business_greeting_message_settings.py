from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessRecipients


@dataclass(kw_only=True)
class BusinessGreetingMessageSettings(BaseType):
    """
    Describes settings for greeting messages that are automatically sent by a Telegram Business account as response to incoming messages in an inactive private chat
    """

    __type__: Literal["businessGreetingMessageSettings"] = "businessGreetingMessageSettings"

    shortcut_id: int
    """Unique quick reply shortcut identifier for the greeting messages"""
    recipients: BusinessRecipients
    """Chosen recipients of the greeting messages"""
    inactivity_days: int
    """The number of days after which a chat will be considered as inactive; currently, must be on of 7, 14, 21, or 28"""
