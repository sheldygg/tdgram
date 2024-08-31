from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClearRecentlyFoundChats(BaseMethod):
    """
    Clears the list of recently found chats
    """

    __type__: Literal["clearRecentlyFoundChats"] = "clearRecentlyFoundChats"
    __returning_type__ = Ok
