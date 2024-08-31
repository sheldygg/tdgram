from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ScopeAutosaveSettings


@dataclass(kw_only=True)
class AutosaveSettingsException(BaseType):
    """
    Contains autosave settings for a chat, which overrides default settings for the corresponding scope
    """

    __type__: Literal["autosaveSettingsException"] = "autosaveSettingsException"

    chat_id: int
    """Chat identifier"""
    settings: ScopeAutosaveSettings
    """Autosave settings for the chat"""
