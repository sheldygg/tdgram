from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureGreetingMessage(BaseType):
    """
    The ability to set up a greeting message
    """

    __type__: Literal["businessFeatureGreetingMessage"] = "businessFeatureGreetingMessage"
