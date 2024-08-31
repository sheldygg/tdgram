from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeApple(BaseType):
    """
    The session is running on a generic Apple device
    """

    __type__: Literal["sessionTypeApple"] = "sessionTypeApple"
