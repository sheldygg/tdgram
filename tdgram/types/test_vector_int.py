from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TestVectorInt(BaseType):
    """
    A simple object containing a vector of numbers; for testing only
    """

    __type__: Literal["testVectorInt"] = "testVectorInt"

    value: list[int]
    """Vector of numbers"""
