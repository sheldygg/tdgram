from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import JsonValue
from .base import BaseMethod


@dataclass(kw_only=True)
class GetJsonValue(BaseMethod):
    """
    Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously
    """

    __type__: Literal["getJsonValue"] = "getJsonValue"
    __returning_type__ = JsonValue

    json: str
    """The JSON-serialized string"""
