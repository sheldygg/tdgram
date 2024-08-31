from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSchedulingStateSendWhenOnline(BaseType):
    """
    The message will be sent when the other user is online. Applicable to private chats only and when the exact online status of the other user is known
    """

    __type__: Literal["messageSchedulingStateSendWhenOnline"] = (
        "messageSchedulingStateSendWhenOnline"
    )
