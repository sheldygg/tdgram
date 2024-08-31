from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Thumbnail, Venue


@dataclass(kw_only=True)
class InlineQueryResultVenue(BaseType):
    """
    Represents information about a venue
    """

    __type__: Literal["inlineQueryResultVenue"] = "inlineQueryResultVenue"

    id: str
    """Unique identifier of the query result"""
    venue: Venue
    """Venue result"""
    thumbnail: Thumbnail | None = None
    """Result thumbnail in JPEG format; may be null"""
