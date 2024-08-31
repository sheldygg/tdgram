from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Venue


@dataclass(kw_only=True)
class MessageVenue(BaseType):
    """
    A message with information about a venue
    """

    __type__: Literal["messageVenue"] = "messageVenue"

    venue: Venue
    """The venue description"""
