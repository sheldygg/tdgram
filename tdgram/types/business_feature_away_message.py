from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureAwayMessage(BaseType):
    """
    The ability to set up an away message
    """

    __type__: Literal["businessFeatureAwayMessage"] = "businessFeatureAwayMessage"
