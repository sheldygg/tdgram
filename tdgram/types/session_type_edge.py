from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeEdge(BaseType):
    """
    The session is running on the Edge browser
    """

    __type__: Literal["sessionTypeEdge"] = "sessionTypeEdge"
