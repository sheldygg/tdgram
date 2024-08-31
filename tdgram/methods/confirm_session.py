from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ConfirmSession(BaseMethod):
    """
    Confirms an unconfirmed session of the current user from another device
    """

    __type__: Literal["confirmSession"] = "confirmSession"
    __returning_type__ = Ok

    session_id: int
    """Session identifier"""
