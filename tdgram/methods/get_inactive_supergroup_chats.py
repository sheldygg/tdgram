from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetInactiveSupergroupChats(BaseMethod):
    """
    Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error. Also, the limit can be increased with Telegram Premium
    """

    __type__: Literal["getInactiveSupergroupChats"] = "getInactiveSupergroupChats"
    __returning_type__ = Chats
