from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SuggestedAction


@dataclass(kw_only=True)
class UpdateSuggestedActions(BaseType):
    """
    The list of suggested to the user actions has changed
    """

    __type__: Literal["updateSuggestedActions"] = "updateSuggestedActions"

    added_actions: list[SuggestedAction]
    """Added suggested actions"""
    removed_actions: list[SuggestedAction]
    """Removed suggested actions"""
