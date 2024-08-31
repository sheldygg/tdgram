from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Users
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRecentInlineBots(BaseMethod):
    """
    Returns up to 20 recently used inline bots in the order of their last usage
    """

    __type__: Literal["getRecentInlineBots"] = "getRecentInlineBots"
    __returning_type__ = Users
