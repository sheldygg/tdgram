from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats, PublicChatType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCreatedPublicChats(BaseMethod):
    """
    Returns a list of public chats of the specified type, owned by the user
    """

    __type__: Literal["getCreatedPublicChats"] = "getCreatedPublicChats"
    __returning_type__ = Chats

    type: PublicChatType
    """Type of the public chats to return"""
