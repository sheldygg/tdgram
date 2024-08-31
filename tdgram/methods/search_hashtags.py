from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Hashtags
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchHashtags(BaseMethod):
    """
    Searches for recently used hashtags by their prefix
    """

    __type__: Literal["searchHashtags"] = "searchHashtags"
    __returning_type__ = Hashtags

    prefix: str
    """Hashtag prefix to search for"""
    limit: int
    """The maximum number of hashtags to be returned"""
