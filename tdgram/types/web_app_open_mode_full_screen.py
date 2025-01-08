from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class WebAppOpenModeFullScreen(BaseType):
    """
    The Web App is opened in the full-screen mode
    """

    __type__: Literal["webAppOpenModeFullScreen"] = "webAppOpenModeFullScreen"
