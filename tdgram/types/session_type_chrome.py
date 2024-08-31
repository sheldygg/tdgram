from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeChrome(BaseType):
    """
    The session is running on the Chrome browser
    """

    __type__: Literal["sessionTypeChrome"] = "sessionTypeChrome"
