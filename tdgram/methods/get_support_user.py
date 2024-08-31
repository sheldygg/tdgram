from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import User
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSupportUser(BaseMethod):
    """
    Returns a user that can be contacted to get support
    """

    __type__: Literal["getSupportUser"] = "getSupportUser"
    __returning_type__ = User
