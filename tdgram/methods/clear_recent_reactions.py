from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClearRecentReactions(BaseMethod):
    """
    Clears the list of recently used reactions
    """

    __type__: Literal["clearRecentReactions"] = "clearRecentReactions"
    __returning_type__ = Ok
