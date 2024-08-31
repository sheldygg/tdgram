from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InlineQueryResult, InlineQueryResultsButton


@dataclass(kw_only=True)
class InlineQueryResults(BaseType):
    """
    Represents the results of the inline query. Use sendInlineQueryResultMessage to send the result of the query
    """

    __type__: Literal["inlineQueryResults"] = "inlineQueryResults"

    inline_query_id: int
    """Unique identifier of the inline query"""
    button: InlineQueryResultsButton | None = None
    """Button to be shown above inline query results; may be null"""
    results: list[InlineQueryResult]
    """Results of the query"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""
