from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Venue


@dataclass(kw_only=True)
class InputMessageVenue(BaseType):
    """
    A message with information about a venue
    """

    __type__: Literal["inputMessageVenue"] = "inputMessageVenue"

    venue: Venue
    """Venue to send"""
