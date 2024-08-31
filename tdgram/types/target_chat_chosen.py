from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TargetChatChosen(BaseType):
    """
    The chat needs to be chosen by the user among chats of the specified types
    """

    __type__: Literal["targetChatChosen"] = "targetChatChosen"

    allow_user_chats: bool
    """True, if private chats with ordinary users are allowed"""
    allow_bot_chats: bool
    """True, if private chats with other bots are allowed"""
    allow_group_chats: bool
    """True, if basic group and supergroup chats are allowed"""
    allow_channel_chats: bool
    """True, if channel chats are allowed"""
