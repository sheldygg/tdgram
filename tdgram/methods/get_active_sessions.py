from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Sessions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetActiveSessions(BaseMethod):
    """
    Returns all active sessions of the current user
    """

    __type__: Literal["getActiveSessions"] = "getActiveSessions"
    __returning_type__ = Sessions
