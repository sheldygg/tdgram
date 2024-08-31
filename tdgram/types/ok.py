from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Ok(BaseType):
    """
    An object of this type is returned on a successful function call for certain functions
    """

    __type__: Literal["ok"] = "ok"
