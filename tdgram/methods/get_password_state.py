from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPasswordState(BaseMethod):
    """
    Returns the current state of 2-step verification
    """

    __type__: Literal["getPasswordState"] = "getPasswordState"
    __returning_type__ = PasswordState
