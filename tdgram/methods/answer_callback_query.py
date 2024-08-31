from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AnswerCallbackQuery(BaseMethod):
    """
    Sets the result of a callback query; for bots only
    """

    __type__: Literal["answerCallbackQuery"] = "answerCallbackQuery"
    __returning_type__ = Ok

    callback_query_id: int
    """Identifier of the callback query"""
    text: str
    """Text of the answer"""
    show_alert: bool
    """Pass true to show an alert to the user instead of a toast notification"""
    url: str
    """URL to be opened"""
    cache_time: int
    """Time during which the result of the query can be cached, in seconds"""
