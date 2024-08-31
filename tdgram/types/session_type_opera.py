from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeOpera(BaseType):
    """
    The session is running on the Opera browser
    """

    __type__: Literal["sessionTypeOpera"] = "sessionTypeOpera"
