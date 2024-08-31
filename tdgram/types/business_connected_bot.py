from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessRecipients


@dataclass(kw_only=True)
class BusinessConnectedBot(BaseType):
    """
    Describes a bot connected to a business account
    """

    __type__: Literal["businessConnectedBot"] = "businessConnectedBot"

    bot_user_id: int
    """User identifier of the bot"""
    recipients: BusinessRecipients
    """Private chats that will be accessible to the bot"""
    can_reply: bool
    """True, if the bot can send messages to the private chats; false otherwise"""
