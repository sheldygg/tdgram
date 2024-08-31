from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Point


@dataclass(kw_only=True)
class VectorPathCommandLine(BaseType):
    """
    A straight line to a given point
    """

    __type__: Literal["vectorPathCommandLine"] = "vectorPathCommandLine"

    end_point: Point
    """The end point of the straight line"""
