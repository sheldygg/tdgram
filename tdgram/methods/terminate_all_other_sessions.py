from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class TerminateAllOtherSessions(BaseMethod):
    """
    Terminates all other sessions of the current user
    """

    __type__: Literal["terminateAllOtherSessions"] = "terminateAllOtherSessions"
    __returning_type__ = Ok
