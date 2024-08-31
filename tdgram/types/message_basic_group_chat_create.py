from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageBasicGroupChatCreate(BaseType):
    """
    A newly created basic group
    """

    __type__: Literal["messageBasicGroupChatCreate"] = "messageBasicGroupChatCreate"

    title: str
    """Title of the basic group"""
    member_user_ids: list[int]
    """User identifiers of members in the basic group"""
