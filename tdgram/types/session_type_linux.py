from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SessionTypeLinux(BaseType):
    """
    The session is running on a Linux device
    """

    __type__: Literal["sessionTypeLinux"] = "sessionTypeLinux"
