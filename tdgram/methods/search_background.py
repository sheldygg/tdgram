from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Background
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchBackground(BaseMethod):
    """
    Searches for a background by its name
    """

    __type__: Literal["searchBackground"] = "searchBackground"
    __returning_type__ = Background

    name: str
    """The name of the background"""
