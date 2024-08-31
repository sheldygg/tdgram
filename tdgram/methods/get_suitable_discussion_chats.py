from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSuitableDiscussionChats(BaseMethod):
    """
    Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group.
    """

    __type__: Literal["getSuitableDiscussionChats"] = "getSuitableDiscussionChats"
    __returning_type__ = Chats
