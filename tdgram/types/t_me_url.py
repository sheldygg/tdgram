from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TMeUrlType


@dataclass(kw_only=True)
class TMeUrl(BaseType):
    """
    Represents a URL linking to an internal Telegram entity
    """

    __type__: Literal["tMeUrl"] = "tMeUrl"

    url: str
    """URL"""
    type: TMeUrlType
    """Type of the URL"""
