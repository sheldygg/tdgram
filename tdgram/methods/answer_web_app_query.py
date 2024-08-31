from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputInlineQueryResult, SentWebAppMessage
from .base import BaseMethod


@dataclass(kw_only=True)
class AnswerWebAppQuery(BaseMethod):
    """
    Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only
    """

    __type__: Literal["answerWebAppQuery"] = "answerWebAppQuery"
    __returning_type__ = SentWebAppMessage

    web_app_query_id: str
    """Identifier of the Web App query"""
    result: InputInlineQueryResult
    """The result of the query"""
