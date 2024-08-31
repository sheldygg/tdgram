from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SavedMessagesTopic


@dataclass(kw_only=True)
class UpdateSavedMessagesTopic(BaseType):
    """
    Basic information about a Saved Messages topic has changed. This update is guaranteed to come before the topic identifier is returned to the application
    """

    __type__: Literal["updateSavedMessagesTopic"] = "updateSavedMessagesTopic"

    topic: SavedMessagesTopic
    """New data about the topic"""
