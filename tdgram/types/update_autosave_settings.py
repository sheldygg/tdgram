from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AutosaveSettingsScope, ScopeAutosaveSettings


@dataclass(kw_only=True)
class UpdateAutosaveSettings(BaseType):
    """
    Autosave settings for some type of chats were updated
    """

    __type__: Literal["updateAutosaveSettings"] = "updateAutosaveSettings"

    scope: AutosaveSettingsScope
    """Type of chats for which autosave settings were updated"""
    settings: ScopeAutosaveSettings | None = None
    """The new autosave settings; may be null if the settings are reset to default"""
