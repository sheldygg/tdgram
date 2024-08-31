from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import JsonObjectMember


@dataclass(kw_only=True)
class JsonValueObject(BaseType):
    """
    Represents a JSON object
    """

    __type__: Literal["jsonValueObject"] = "jsonValueObject"

    members: list[JsonObjectMember]
    """The list of object members"""
