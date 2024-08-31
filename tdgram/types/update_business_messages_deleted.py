from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateBusinessMessagesDeleted(BaseType):
    """
    Messages in a business account were deleted; for bots only
    """

    __type__: Literal["updateBusinessMessagesDeleted"] = "updateBusinessMessagesDeleted"

    connection_id: str
    """Unique identifier of the business connection"""
    chat_id: int
    """Identifier of a chat in the business account in which messages were deleted"""
    message_ids: list[int]
    """Unique message identifiers of the deleted messages"""
