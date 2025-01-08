from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import VectorPathCommand


@dataclass(kw_only=True)
class ClosedVectorPath(BaseType):
    """
    Represents a closed vector path. The path begins at the end point of the last command. The coordinate system origin is in the upper-left corner
    """

    __type__: Literal["closedVectorPath"] = "closedVectorPath"

    commands: list[VectorPathCommand]
    """List of vector path commands"""
