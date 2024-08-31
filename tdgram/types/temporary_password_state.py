from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TemporaryPasswordState(BaseType):
    """
    Returns information about the availability of a temporary password, which can be used for payments
    """

    __type__: Literal["temporaryPasswordState"] = "temporaryPasswordState"

    has_password: bool
    """True, if a temporary password is available"""
    valid_for: int
    """Time left before the temporary password expires, in seconds"""
