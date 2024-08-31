from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TextEntityType


@dataclass(kw_only=True)
class TextEntity(BaseType):
    """
    Represents a part of the text that needs to be formatted in some unusual way
    """

    __type__: Literal["textEntity"] = "textEntity"

    offset: int
    """Offset of the entity, in UTF-16 code units"""
    length: int
    """Length of the entity, in UTF-16 code units"""
    type: TextEntityType
    """Type of the entity"""
