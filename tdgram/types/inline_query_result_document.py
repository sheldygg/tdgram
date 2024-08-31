from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Document


@dataclass(kw_only=True)
class InlineQueryResultDocument(BaseType):
    """
    Represents a document
    """

    __type__: Literal["inlineQueryResultDocument"] = "inlineQueryResultDocument"

    id: str
    """Unique identifier of the query result"""
    document: Document
    """Document"""
    title: str
    """Document title"""
    description: str
    """Document description"""
