from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatType, Location


@dataclass(kw_only=True)
class UpdateNewInlineQuery(BaseType):
    """
    A new incoming inline query; for bots only
    """

    __type__: Literal["updateNewInlineQuery"] = "updateNewInlineQuery"

    id: int
    """Unique query identifier"""
    sender_user_id: int
    """Identifier of the user who sent the query"""
    user_location: Location | None = None
    """User location; may be null"""
    chat_type: ChatType | None = None
    """The type of the chat from which the query originated; may be null if unknown"""
    query: str
    """Text of the query"""
    offset: str
    """Offset of the first entry to return"""
