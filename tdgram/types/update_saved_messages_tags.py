from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SavedMessagesTags


@dataclass(kw_only=True)
class UpdateSavedMessagesTags(BaseType):
    """
    Tags used in Saved Messages or a Saved Messages topic have changed
    """

    __type__: Literal["updateSavedMessagesTags"] = "updateSavedMessagesTags"

    saved_messages_topic_id: int
    """Identifier of Saved Messages topic which tags were changed; 0 if tags for the whole chat has changed"""
    tags: SavedMessagesTags
    """The new tags"""
