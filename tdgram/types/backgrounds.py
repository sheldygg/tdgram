from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Background


@dataclass(kw_only=True)
class Backgrounds(BaseType):
    """
    Contains a list of backgrounds
    """

    __type__: Literal["backgrounds"] = "backgrounds"

    backgrounds: list[Background]
    """A list of backgrounds"""
