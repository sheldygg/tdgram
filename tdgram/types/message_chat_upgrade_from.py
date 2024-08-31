from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatUpgradeFrom(BaseType):
    """
    A supergroup has been created from a basic group
    """

    __type__: Literal["messageChatUpgradeFrom"] = "messageChatUpgradeFrom"

    title: str
    """Title of the newly created supergroup"""
    basic_group_id: int
    """The identifier of the original basic group"""
