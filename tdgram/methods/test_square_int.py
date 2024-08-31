from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TestInt
from .base import BaseMethod


@dataclass(kw_only=True)
class TestSquareInt(BaseMethod):
    """
    Returns the squared received number; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testSquareInt"] = "testSquareInt"
    __returning_type__ = TestInt

    x: int
    """Number to square"""
