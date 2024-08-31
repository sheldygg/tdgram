from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InlineQueryResultsButton, InputInlineQueryResult, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AnswerInlineQuery(BaseMethod):
    """
    Sets the result of an inline query; for bots only
    """

    __type__: Literal["answerInlineQuery"] = "answerInlineQuery"
    __returning_type__ = Ok

    inline_query_id: int
    """Identifier of the inline query"""
    is_personal: bool
    """Pass true if results may be cached and returned only for the user that sent the query. By default, results may be returned to any user who sends the same query"""
    button: InlineQueryResultsButton | None = None
    """Button to be shown above inline query results; pass null if none"""
    results: list[InputInlineQueryResult]
    """The results of the query"""
    cache_time: int
    """Allowed time to cache the results of the query, in seconds"""
    next_offset: str
    """Offset for the next inline query; pass an empty string if there are no more results"""
