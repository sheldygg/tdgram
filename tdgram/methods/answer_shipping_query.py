from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ShippingOption
from .base import BaseMethod


@dataclass(kw_only=True)
class AnswerShippingQuery(BaseMethod):
    """
    Sets the result of a shipping query; for bots only
    """

    __type__: Literal["answerShippingQuery"] = "answerShippingQuery"
    __returning_type__ = Ok

    shipping_query_id: int
    """Identifier of the shipping query"""
    shipping_options: list[ShippingOption]
    """Available shipping options"""
    error_message: str
    """An error message, empty on success"""
