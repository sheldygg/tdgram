from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesChatTypeFilterGroup(BaseType):
    """
    Returns only messages in basic group and supergroup chats
    """

    __type__: Literal["searchMessagesChatTypeFilterGroup"] = "searchMessagesChatTypeFilterGroup"
