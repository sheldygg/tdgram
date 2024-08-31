from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location


@dataclass(kw_only=True)
class Venue(BaseType):
    """
    Describes a venue
    """

    __type__: Literal["venue"] = "venue"

    location: Location
    """Venue location; as defined by the sender"""
    title: str
    """Venue name; as defined by the sender"""
    address: str
    """Venue address; as defined by the sender"""
    provider: str
    """Provider of the venue database; as defined by the sender. Currently, only 'foursquare' and 'gplaces' (Google Places) need to be supported"""
    id: str
    """Identifier of the venue in the provider database; as defined by the sender"""
    type: str
    """Type of the venue in the provider database; as defined by the sender"""
