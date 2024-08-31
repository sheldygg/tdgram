from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AutosaveSettings
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAutosaveSettings(BaseMethod):
    """
    Returns autosave settings for the current user
    """

    __type__: Literal["getAutosaveSettings"] = "getAutosaveSettings"
    __returning_type__ = AutosaveSettings
