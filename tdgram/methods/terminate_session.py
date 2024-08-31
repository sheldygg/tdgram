from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class TerminateSession(BaseMethod):
    """
    Terminates a session of the current user
    """

    __type__: Literal["terminateSession"] = "terminateSession"
    __returning_type__ = Ok

    session_id: int
    """Session identifier"""
