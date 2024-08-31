from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AnswerCustomQuery(BaseMethod):
    """
    Answers a custom query; for bots only
    """

    __type__: Literal["answerCustomQuery"] = "answerCustomQuery"
    __returning_type__ = Ok

    custom_query_id: int
    """Identifier of a custom query"""
    data: str
    """JSON-serialized answer to the query"""
