from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeXbox(BaseType):
    """
    The session is running on an Xbox console
    """

    __type__: Literal["sessionTypeXbox"] = "sessionTypeXbox"
