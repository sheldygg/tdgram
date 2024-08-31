from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ResetInstalledBackgrounds(BaseMethod):
    """
    Resets list of installed backgrounds to its default value
    """

    __type__: Literal["resetInstalledBackgrounds"] = "resetInstalledBackgrounds"
    __returning_type__ = Ok
