from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import SavedMessagesTags
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSavedMessagesTags(BaseMethod):
    """
    Returns tags used in Saved Messages or a Saved Messages topic
    """

    __type__: Literal["getSavedMessagesTags"] = "getSavedMessagesTags"
    __returning_type__ = SavedMessagesTags

    saved_messages_topic_id: int
    """Identifier of Saved Messages topic which tags will be returned; pass 0 to get all Saved Messages tags"""
