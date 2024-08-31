from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveRecentHashtag(BaseMethod):
    """
    Removes a hashtag from the list of recently used hashtags
    """

    __type__: Literal["removeRecentHashtag"] = "removeRecentHashtag"
    __returning_type__ = Ok

    hashtag: str
    """Hashtag to delete"""
