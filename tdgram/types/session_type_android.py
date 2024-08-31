from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeAndroid(BaseType):
    """
    The session is running on an Android device
    """

    __type__: Literal["sessionTypeAndroid"] = "sessionTypeAndroid"
