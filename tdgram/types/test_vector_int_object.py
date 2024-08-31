from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TestInt


@dataclass(kw_only=True)
class TestVectorIntObject(BaseType):
    """
    A simple object containing a vector of objects that hold a number; for testing only
    """

    __type__: Literal["testVectorIntObject"] = "testVectorIntObject"

    value: list[TestInt]
    """Vector of objects"""
