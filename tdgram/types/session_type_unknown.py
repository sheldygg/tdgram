from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeUnknown(BaseType):
    """
    The session is running on an unknown type of device
    """

    __type__: Literal["sessionTypeUnknown"] = "sessionTypeUnknown"
