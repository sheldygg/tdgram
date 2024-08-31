from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterFailedToSend(BaseType):
    """
    Returns only failed to send messages. This filter can be used only if the message database is used
    """

    __type__: Literal["searchMessagesFilterFailedToSend"] = "searchMessagesFilterFailedToSend"
