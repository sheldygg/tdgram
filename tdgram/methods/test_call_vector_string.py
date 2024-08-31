from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TestVectorString
from .base import BaseMethod


@dataclass(kw_only=True)
class TestCallVectorString(BaseMethod):
    """
    Returns the received vector of strings; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testCallVectorString"] = "testCallVectorString"
    __returning_type__ = TestVectorString

    x: list[str]
    """Vector of strings to return"""
