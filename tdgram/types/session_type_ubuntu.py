from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeUbuntu(BaseType):
    """
    The session is running on an Ubuntu device
    """

    __type__: Literal["sessionTypeUbuntu"] = "sessionTypeUbuntu"
