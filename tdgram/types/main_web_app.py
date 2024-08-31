from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MainWebApp(BaseType):
    """
    Contains information about the main Web App of a bot
    """

    __type__: Literal["mainWebApp"] = "mainWebApp"

    url: str
    """URL of the Web App to open"""
    is_compact: bool
    """True, if the Web App must always be opened in the compact mode instead of the full-size mode"""
