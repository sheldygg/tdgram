from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AutosaveSettingsScopePrivateChats(BaseType):
    """
    Autosave settings applied to all private chats without chat-specific settings
    """

    __type__: Literal["autosaveSettingsScopePrivateChats"] = "autosaveSettingsScopePrivateChats"
