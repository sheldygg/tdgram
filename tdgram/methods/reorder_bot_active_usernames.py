from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReorderBotActiveUsernames(BaseMethod):
    """
    Changes order of active usernames of a bot. Can be called only if userTypeBot.can_be_edited == true
    """

    __type__: Literal["reorderBotActiveUsernames"] = "reorderBotActiveUsernames"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the target bot"""
    usernames: list[str]
    """The new order of active usernames. All currently active usernames must be specified"""
