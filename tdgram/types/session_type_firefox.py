from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeFirefox(BaseType):
    """
    The session is running on the Firefox browser
    """

    __type__: Literal["sessionTypeFirefox"] = "sessionTypeFirefox"
