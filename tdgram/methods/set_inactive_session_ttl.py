from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetInactiveSessionTtl(BaseMethod):
    """
    Changes the period of inactivity after which sessions will automatically be terminated
    """

    __type__: Literal["setInactiveSessionTtl"] = "setInactiveSessionTtl"
    __returning_type__ = Ok

    inactive_session_ttl_days: int
    """New number of days of inactivity before sessions will be automatically terminated; 1-366 days"""
