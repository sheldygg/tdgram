from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatUpgradeTo(BaseType):
    """
    A basic group was upgraded to a supergroup and was deactivated as the result
    """

    __type__: Literal["messageChatUpgradeTo"] = "messageChatUpgradeTo"

    supergroup_id: int
    """Identifier of the supergroup to which the basic group was upgraded"""
