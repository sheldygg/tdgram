from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotWriteAccessAllowReasonAddedToAttachmentMenu(BaseType):
    """
    The user added the bot to attachment or side menu using toggleBotIsAddedToAttachmentMenu
    """

    __type__: Literal["botWriteAccessAllowReasonAddedToAttachmentMenu"] = (
        "botWriteAccessAllowReasonAddedToAttachmentMenu"
    )
