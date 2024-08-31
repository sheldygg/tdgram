from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeBrave(BaseType):
    """
    The session is running on the Brave browser
    """

    __type__: Literal["sessionTypeBrave"] = "sessionTypeBrave"
