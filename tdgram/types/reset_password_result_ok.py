from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ResetPasswordResultOk(BaseType):
    """
    The password was reset
    """

    __type__: Literal["resetPasswordResultOk"] = "resetPasswordResultOk"
