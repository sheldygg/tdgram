from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TestVectorString(BaseType):
    """
    A simple object containing a vector of strings; for testing only
    """

    __type__: Literal["testVectorString"] = "testVectorString"

    value: list[str]
    """Vector of strings"""
