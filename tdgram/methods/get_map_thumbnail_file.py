from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import File, Location
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMapThumbnailFile(BaseMethod):
    """
    Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded
    """

    __type__: Literal["getMapThumbnailFile"] = "getMapThumbnailFile"
    __returning_type__ = File

    location: Location
    """Location of the map center"""
    zoom: int
    """Map zoom level; 13-20"""
    width: int
    """Map width in pixels before applying scale; 16-1024"""
    height: int
    """Map height in pixels before applying scale; 16-1024"""
    scale: int
    """Map scale; 1-3"""
    chat_id: int
    """Identifier of a chat in which the thumbnail will be shown. Use 0 if unknown"""
