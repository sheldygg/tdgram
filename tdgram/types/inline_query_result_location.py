from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location, Thumbnail


@dataclass(kw_only=True)
class InlineQueryResultLocation(BaseType):
    """
    Represents a point on the map
    """

    __type__: Literal["inlineQueryResultLocation"] = "inlineQueryResultLocation"

    id: str
    """Unique identifier of the query result"""
    location: Location
    """Location result"""
    title: str
    """Title of the result"""
    thumbnail: Thumbnail | None = None
    """Result thumbnail in JPEG format; may be null"""
