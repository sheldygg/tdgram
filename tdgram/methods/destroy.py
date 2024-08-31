from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class Destroy(BaseMethod):
    """
    Closes the TDLib instance, destroying all local data without a proper logout. The current user session will remain in the list of all active sessions. All local data will be destroyed.
    """

    __type__: Literal["destroy"] = "destroy"
    __returning_type__ = Ok
