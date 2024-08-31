from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TextEntity


@dataclass(kw_only=True)
class FormattedText(BaseType):
    """
    A text with some entities
    """

    __type__: Literal["formattedText"] = "formattedText"

    text: str
    """The text"""
    entities: list[TextEntity]
    """Entities contained in the text. Entities can be nested, but must not mutually intersect with each other."""
