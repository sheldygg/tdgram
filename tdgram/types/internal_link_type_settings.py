from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeSettings(BaseType):
    """
    The link is a link to application settings
    """

    __type__: Literal["internalLinkTypeSettings"] = "internalLinkTypeSettings"
