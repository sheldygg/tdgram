from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import JsonValue


@dataclass(kw_only=True)
class JsonObjectMember(BaseType):
    """
    Represents one member of a JSON object
    """

    __type__: Literal["jsonObjectMember"] = "jsonObjectMember"

    key: str
    """Member's key"""
    value: JsonValue
    """Member's value"""
