from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotWriteAccessAllowReasonAcceptedRequest(BaseType):
    """
    The user accepted bot's request to send messages with allowBotToSendMessages
    """

    __type__: Literal["botWriteAccessAllowReasonAcceptedRequest"] = (
        "botWriteAccessAllowReasonAcceptedRequest"
    )
