from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location, LocationAddress


@dataclass(kw_only=True)
class StoryAreaTypeLocation(BaseType):
    """
    An area pointing to a location
    """

    __type__: Literal["storyAreaTypeLocation"] = "storyAreaTypeLocation"

    location: Location
    """The location"""
    address: LocationAddress | None = None
    """Address of the location; may be null if unknown"""
