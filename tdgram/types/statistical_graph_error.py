from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StatisticalGraphError(BaseType):
    """
    An error message to be shown to the user instead of the graph
    """

    __type__: Literal["statisticalGraphError"] = "statisticalGraphError"

    error_message: str
    """The error message"""
