from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AnswerPreCheckoutQuery(BaseMethod):
    """
    Sets the result of a pre-checkout query; for bots only
    """

    __type__: Literal["answerPreCheckoutQuery"] = "answerPreCheckoutQuery"
    __returning_type__ = Ok

    pre_checkout_query_id: int
    """Identifier of the pre-checkout query"""
    error_message: str
    """An error message, empty on success"""
