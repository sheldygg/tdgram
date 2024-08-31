from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeTheme(BaseType):
    """
    The link is a link to a cloud theme. TDLib has no theme support yet
    """

    __type__: Literal["internalLinkTypeTheme"] = "internalLinkTypeTheme"

    theme_name: str
    """Name of the theme"""
