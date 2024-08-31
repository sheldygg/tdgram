from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSessionCanAcceptCalls(BaseMethod):
    """
    Toggles whether a session can accept incoming calls
    """

    __type__: Literal["toggleSessionCanAcceptCalls"] = "toggleSessionCanAcceptCalls"
    __returning_type__ = Ok

    session_id: int
    """Session identifier"""
    can_accept_calls: bool
    """Pass true to allow accepting incoming calls by the session; pass false otherwise"""
