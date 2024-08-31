from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputStoryAreaTypePreviousVenue(BaseType):
    """
    An area pointing to a venue already added to the story
    """

    __type__: Literal["inputStoryAreaTypePreviousVenue"] = "inputStoryAreaTypePreviousVenue"

    venue_provider: str
    """Provider of the venue"""
    venue_id: str
    """Identifier of the venue in the provider database"""
