from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterPhoto(BaseType):
    """
    Returns only photo messages
    """

    __type__: Literal["searchMessagesFilterPhoto"] = "searchMessagesFilterPhoto"
