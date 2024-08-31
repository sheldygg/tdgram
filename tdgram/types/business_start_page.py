from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class BusinessStartPage(BaseType):
    """
    Describes settings for a business account start page
    """

    __type__: Literal["businessStartPage"] = "businessStartPage"

    title: str
    """Title text of the start page"""
    message: str
    """Message text of the start page"""
    sticker: Sticker | None = None
    """Greeting sticker of the start page; may be null if none"""
