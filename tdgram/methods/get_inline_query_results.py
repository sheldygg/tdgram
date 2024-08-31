from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InlineQueryResults, Location
from .base import BaseMethod


@dataclass(kw_only=True)
class GetInlineQueryResults(BaseMethod):
    """
    Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
    """

    __type__: Literal["getInlineQueryResults"] = "getInlineQueryResults"
    __returning_type__ = InlineQueryResults

    bot_user_id: int
    """Identifier of the target bot"""
    chat_id: int
    """Identifier of the chat where the query was sent"""
    user_location: Location | None = None
    """Location of the user; pass null if unknown or the bot doesn't need user's location"""
    query: str
    """Text of the query"""
    offset: str
    """Offset of the first entry to return; use empty string to get the first chunk of results"""
