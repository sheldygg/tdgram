from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeSafari(BaseType):
    """
    The session is running on the Safari browser
    """

    __type__: Literal["sessionTypeSafari"] = "sessionTypeSafari"
