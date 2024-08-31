from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTexts(BaseType):
    """
    A concatenation of rich texts
    """

    __type__: Literal["richTexts"] = "richTexts"

    texts: list[RichText]
    """Texts"""
