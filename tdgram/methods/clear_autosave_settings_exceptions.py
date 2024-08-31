from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClearAutosaveSettingsExceptions(BaseMethod):
    """
    Clears the list of all autosave settings exceptions. The method is guaranteed to work only after at least one call to getAutosaveSettings
    """

    __type__: Literal["clearAutosaveSettingsExceptions"] = "clearAutosaveSettingsExceptions"
    __returning_type__ = Ok
