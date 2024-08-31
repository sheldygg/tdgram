from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class UpgradeBasicGroupChatToSupergroupChat(BaseMethod):
    """
    Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires owner privileges. Deactivates the original basic group
    """

    __type__: Literal["upgradeBasicGroupChatToSupergroupChat"] = (
        "upgradeBasicGroupChatToSupergroupChat"
    )
    __returning_type__ = Chat

    chat_id: int
    """Identifier of the chat to upgrade"""
