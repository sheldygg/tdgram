from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeVivaldi(BaseType):
    """
    The session is running on the Vivaldi browser
    """

    __type__: Literal["sessionTypeVivaldi"] = "sessionTypeVivaldi"
