from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AutosaveSettingsScopeChannelChats(BaseType):
    """
    Autosave settings applied to all channel chats without chat-specific settings
    """

    __type__: Literal["autosaveSettingsScopeChannelChats"] = "autosaveSettingsScopeChannelChats"
