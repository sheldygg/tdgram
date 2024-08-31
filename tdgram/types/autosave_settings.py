from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AutosaveSettingsException, ScopeAutosaveSettings


@dataclass(kw_only=True)
class AutosaveSettings(BaseType):
    """
    Describes autosave settings
    """

    __type__: Literal["autosaveSettings"] = "autosaveSettings"

    private_chat_settings: ScopeAutosaveSettings
    """Default autosave settings for private chats"""
    group_settings: ScopeAutosaveSettings
    """Default autosave settings for basic group and supergroup chats"""
    channel_settings: ScopeAutosaveSettings
    """Default autosave settings for channel chats"""
    exceptions: list[AutosaveSettingsException]
    """Autosave settings for specific chats"""
