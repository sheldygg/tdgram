from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Venue


@dataclass(kw_only=True)
class StoryAreaTypeVenue(BaseType):
    """
    An area pointing to a venue
    """

    __type__: Literal["storyAreaTypeVenue"] = "storyAreaTypeVenue"

    venue: Venue
    """Information about the venue"""
