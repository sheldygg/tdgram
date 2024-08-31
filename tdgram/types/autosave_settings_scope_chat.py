from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AutosaveSettingsScopeChat(BaseType):
    """
    Autosave settings applied to a chat
    """

    __type__: Literal["autosaveSettingsScopeChat"] = "autosaveSettingsScopeChat"

    chat_id: int
    """Chat identifier"""
