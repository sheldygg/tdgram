from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Point


@dataclass(kw_only=True)
class VectorPathCommandCubicBezierCurve(BaseType):
    """
    A cubic Bézier curve to a given point
    """

    __type__: Literal["vectorPathCommandCubicBezierCurve"] = "vectorPathCommandCubicBezierCurve"

    start_control_point: Point
    """The start control point of the curve"""
    end_control_point: Point
    """The end control point of the curve"""
    end_point: Point
    """The end point of the curve"""
