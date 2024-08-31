from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TestVectorInt
from .base import BaseMethod


@dataclass(kw_only=True)
class TestCallVectorInt(BaseMethod):
    """
    Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testCallVectorInt"] = "testCallVectorInt"
    __returning_type__ = TestVectorInt

    x: list[int]
    """Vector of numbers to return"""
