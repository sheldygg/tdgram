from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClearSearchedForTags(BaseMethod):
    """
    Clears the list of recently searched for hashtags or cashtags
    """

    __type__: Literal["clearSearchedForTags"] = "clearSearchedForTags"
    __returning_type__ = Ok

    clear_cashtags: bool
    """Pass true to clear the list of recently searched for cashtags; otherwise, the list of recently searched for hashtags will be cleared"""
