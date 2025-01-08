from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesChatTypeFilterChannel(BaseType):
    """
    Returns only messages in channel chats
    """

    __type__: Literal["searchMessagesChatTypeFilterChannel"] = (
        "searchMessagesChatTypeFilterChannel"
    )
