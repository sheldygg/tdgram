from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateDeleteMessages(BaseType):
    """
    Some messages were deleted
    """

    __type__: Literal["updateDeleteMessages"] = "updateDeleteMessages"

    chat_id: int
    """Chat identifier"""
    message_ids: list[int]
    """Identifiers of the deleted messages"""
    is_permanent: bool
    """True, if the messages are permanently deleted by a user (as opposed to just becoming inaccessible)"""
    from_cache: bool
    """True, if the messages are deleted only from the cache and can possibly be retrieved again in the future"""
