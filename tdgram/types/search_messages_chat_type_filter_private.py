from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesChatTypeFilterPrivate(BaseType):
    """
    Returns only messages in private chats
    """

    __type__: Literal["searchMessagesChatTypeFilterPrivate"] = (
        "searchMessagesChatTypeFilterPrivate"
    )
