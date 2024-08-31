from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, PublicChatType
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckCreatedPublicChatsLimit(BaseMethod):
    """
    Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached. The limit can be increased with Telegram Premium
    """

    __type__: Literal["checkCreatedPublicChatsLimit"] = "checkCreatedPublicChatsLimit"
    __returning_type__ = Ok

    type: PublicChatType
    """Type of the public chats, for which to check the limit"""
