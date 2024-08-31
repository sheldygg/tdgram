from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Session


@dataclass(kw_only=True)
class Sessions(BaseType):
    """
    Contains a list of sessions
    """

    __type__: Literal["sessions"] = "sessions"

    sessions: list[Session]
    """List of sessions"""
    inactive_session_ttl_days: int
    """Number of days of inactivity before sessions will automatically be terminated; 1-366 days"""
