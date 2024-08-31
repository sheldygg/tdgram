from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AutosaveSettingsScopeGroupChats(BaseType):
    """
    Autosave settings applied to all basic group and supergroup chats without chat-specific settings
    """

    __type__: Literal["autosaveSettingsScopeGroupChats"] = "autosaveSettingsScopeGroupChats"
