from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterChatPhoto(BaseType):
    """
    Returns only messages containing chat photos
    """

    __type__: Literal["searchMessagesFilterChatPhoto"] = "searchMessagesFilterChatPhoto"
