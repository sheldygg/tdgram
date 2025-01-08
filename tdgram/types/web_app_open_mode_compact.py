from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class WebAppOpenModeCompact(BaseType):
    """
    The Web App is opened in the compact mode
    """

    __type__: Literal["webAppOpenModeCompact"] = "webAppOpenModeCompact"
