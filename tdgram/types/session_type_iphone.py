from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeIphone(BaseType):
    """
    The session is running on an iPhone device
    """

    __type__: Literal["sessionTypeIphone"] = "sessionTypeIphone"
