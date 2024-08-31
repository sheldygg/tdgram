from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TestInt, TestVectorIntObject
from .base import BaseMethod


@dataclass(kw_only=True)
class TestCallVectorIntObject(BaseMethod):
    """
    Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testCallVectorIntObject"] = "testCallVectorIntObject"
    __returning_type__ = TestVectorIntObject

    x: list[TestInt]
    """Vector of objects to return"""
