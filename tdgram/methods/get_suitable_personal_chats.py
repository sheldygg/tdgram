from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSuitablePersonalChats(BaseMethod):
    """
    Returns a list of channel chats, which can be used as a personal chat
    """

    __type__: Literal["getSuitablePersonalChats"] = "getSuitablePersonalChats"
    __returning_type__ = Chats
