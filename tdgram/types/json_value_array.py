from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import JsonValue


@dataclass(kw_only=True)
class JsonValueArray(BaseType):
    """
    Represents a JSON array
    """

    __type__: Literal["jsonValueArray"] = "jsonValueArray"

    values: list[JsonValue]
    """The list of array elements"""
