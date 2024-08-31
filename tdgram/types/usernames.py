from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Usernames(BaseType):
    """
    Describes usernames assigned to a user, a supergroup, or a channel
    """

    __type__: Literal["usernames"] = "usernames"

    active_usernames: list[str]
    """List of active usernames; the first one must be shown as the primary username. The order of active usernames can be changed with reorderActiveUsernames, reorderBotActiveUsernames or reorderSupergroupActiveUsernames"""
    disabled_usernames: list[str]
    """List of currently disabled usernames; the username can be activated with toggleUsernameIsActive, toggleBotUsernameIsActive, or toggleSupergroupUsernameIsActive"""
    editable_username: str
    """The active username, which can be changed with setUsername or setSupergroupUsername. Information about other active usernames can be received using getCollectibleItemInfo"""
