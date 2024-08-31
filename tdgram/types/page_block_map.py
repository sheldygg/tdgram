from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location, PageBlockCaption


@dataclass(kw_only=True)
class PageBlockMap(BaseType):
    """
    A map
    """

    __type__: Literal["pageBlockMap"] = "pageBlockMap"

    location: Location
    """Location of the map center"""
    zoom: int
    """Map zoom level"""
    width: int
    """Map width"""
    height: int
    """Map height"""
    caption: PageBlockCaption
    """Block caption"""
