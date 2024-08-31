from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterMention(BaseType):
    """
    Returns only messages with mentions of the current user, or messages that are replies to their messages
    """

    __type__: Literal["searchMessagesFilterMention"] = "searchMessagesFilterMention"
