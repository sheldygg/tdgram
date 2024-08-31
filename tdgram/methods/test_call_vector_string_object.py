from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TestString, TestVectorStringObject
from .base import BaseMethod


@dataclass(kw_only=True)
class TestCallVectorStringObject(BaseMethod):
    """
    Returns the received vector of objects containing a string; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testCallVectorStringObject"] = "testCallVectorStringObject"
    __returning_type__ = TestVectorStringObject

    x: list[TestString]
    """Vector of objects to return"""
