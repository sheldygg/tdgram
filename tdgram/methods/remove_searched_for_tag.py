from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveSearchedForTag(BaseMethod):
    """
    Removes a hashtag or a cashtag from the list of recently searched for hashtags or cashtags
    """

    __type__: Literal["removeSearchedForTag"] = "removeSearchedForTag"
    __returning_type__ = Ok

    tag: str
    """Hashtag or cashtag to delete"""
