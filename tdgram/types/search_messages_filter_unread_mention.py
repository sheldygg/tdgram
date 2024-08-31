from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterUnreadMention(BaseType):
    """
    Returns only messages with unread mentions of the current user, or messages that are replies to their messages. When using this filter the results can't be additionally filtered by a query, a message thread or by the sending user
    """

    __type__: Literal["searchMessagesFilterUnreadMention"] = "searchMessagesFilterUnreadMention"
