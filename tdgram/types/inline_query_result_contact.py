from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Contact, Thumbnail


@dataclass(kw_only=True)
class InlineQueryResultContact(BaseType):
    """
    Represents a user contact
    """

    __type__: Literal["inlineQueryResultContact"] = "inlineQueryResultContact"

    id: str
    """Unique identifier of the query result"""
    contact: Contact
    """A user contact"""
    thumbnail: Thumbnail | None = None
    """Result thumbnail in JPEG format; may be null"""
