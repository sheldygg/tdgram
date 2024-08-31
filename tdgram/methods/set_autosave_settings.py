from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AutosaveSettingsScope, Ok, ScopeAutosaveSettings
from .base import BaseMethod


@dataclass(kw_only=True)
class SetAutosaveSettings(BaseMethod):
    """
    Sets autosave settings for the given scope. The method is guaranteed to work only after at least one call to getAutosaveSettings
    """

    __type__: Literal["setAutosaveSettings"] = "setAutosaveSettings"
    __returning_type__ = Ok

    scope: AutosaveSettingsScope
    """Autosave settings scope"""
    settings: ScopeAutosaveSettings | None = None
    """New autosave settings for the scope; pass null to set autosave settings to default"""
