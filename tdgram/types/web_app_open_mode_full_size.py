from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class WebAppOpenModeFullSize(BaseType):
    """
    The Web App is opened in the full-size mode
    """

    __type__: Literal["webAppOpenModeFullSize"] = "webAppOpenModeFullSize"
