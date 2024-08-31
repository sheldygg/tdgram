from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TextEntity


@dataclass(kw_only=True)
class TextEntities(BaseType):
    """
    Contains a list of text entities
    """

    __type__: Literal["textEntities"] = "textEntities"

    entities: list[TextEntity]
    """List of text entities"""
