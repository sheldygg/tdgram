from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeMac(BaseType):
    """
    The session is running on a Mac device
    """

    __type__: Literal["sessionTypeMac"] = "sessionTypeMac"
