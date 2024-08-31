from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TemporaryPasswordState
from .base import BaseMethod


@dataclass(kw_only=True)
class GetTemporaryPasswordState(BaseMethod):
    """
    Returns information about the current temporary password
    """

    __type__: Literal["getTemporaryPasswordState"] = "getTemporaryPasswordState"
    __returning_type__ = TemporaryPasswordState
