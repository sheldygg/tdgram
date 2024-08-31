from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterUrl(BaseType):
    """
    Returns only messages containing URLs
    """

    __type__: Literal["searchMessagesFilterUrl"] = "searchMessagesFilterUrl"
