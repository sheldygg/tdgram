from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ClosedVectorPath


@dataclass(kw_only=True)
class Outline(BaseType):
    """
    Represents outline of an image
    """

    __type__: Literal["outline"] = "outline"

    paths: list[ClosedVectorPath]
    """The list of closed vector paths"""
