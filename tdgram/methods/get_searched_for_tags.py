from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Hashtags
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSearchedForTags(BaseMethod):
    """
    Returns recently searched for hashtags or cashtags by their prefix
    """

    __type__: Literal["getSearchedForTags"] = "getSearchedForTags"
    __returning_type__ = Hashtags

    tag_prefix: str
    """Prefix of hashtags or cashtags to return"""
    limit: int
    """The maximum number of items to be returned"""
