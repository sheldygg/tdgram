from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import JsonValue, Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetJsonString(BaseMethod):
    """
    Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously
    """

    __type__: Literal["getJsonString"] = "getJsonString"
    __returning_type__ = Text

    json_value: JsonValue
    """The JsonValue object"""
