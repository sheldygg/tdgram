from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Users
from .base import BaseMethod


@dataclass(kw_only=True)
class GetOwnedBots(BaseMethod):
    """
    Returns the list of bots owned by the current user
    """

    __type__: Literal["getOwnedBots"] = "getOwnedBots"
    __returning_type__ = Users
