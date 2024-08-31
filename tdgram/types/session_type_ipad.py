from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeIpad(BaseType):
    """
    The session is running on an iPad device
    """

    __type__: Literal["sessionTypeIpad"] = "sessionTypeIpad"
