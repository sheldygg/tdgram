from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, SuggestedAction
from .base import BaseMethod


@dataclass(kw_only=True)
class HideSuggestedAction(BaseMethod):
    """
    Hides a suggested action
    """

    __type__: Literal["hideSuggestedAction"] = "hideSuggestedAction"
    __returning_type__ = Ok

    action: SuggestedAction
    """Suggested action to hide"""
