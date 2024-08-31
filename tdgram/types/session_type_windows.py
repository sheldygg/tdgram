from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeWindows(BaseType):
    """
    The session is running on a Windows device
    """

    __type__: Literal["sessionTypeWindows"] = "sessionTypeWindows"
