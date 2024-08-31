from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MaskPoint


@dataclass(kw_only=True)
class MaskPosition(BaseType):
    """
    Position on a photo where a mask is placed
    """

    __type__: Literal["maskPosition"] = "maskPosition"

    point: MaskPoint
    """Part of the face, relative to which the mask is placed"""
    x_shift: float
    """Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)"""
    y_shift: float
    """Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. (For example, 1.0 will place the mask just below the default mask position)"""
    scale: float
    """Mask scaling coefficient. (For example, 2.0 means a doubled size)"""
