from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TemporaryPasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateTemporaryPassword(BaseMethod):
    """
    Creates a new temporary password for processing payments
    """

    __type__: Literal["createTemporaryPassword"] = "createTemporaryPassword"
    __returning_type__ = TemporaryPasswordState

    password: str
    """The 2-step verification password of the current user"""
    valid_for: int
    """Time during which the temporary password will be valid, in seconds; must be between 60 and 86400"""
