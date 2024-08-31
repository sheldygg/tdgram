from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CustomRequestResult(BaseType):
    """
    Contains the result of a custom request
    """

    __type__: Literal["customRequestResult"] = "customRequestResult"

    result: str
    """A JSON-serialized result"""
