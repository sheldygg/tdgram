from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PassportElement


@dataclass(kw_only=True)
class PassportElements(BaseType):
    """
    Contains information about saved Telegram Passport elements
    """

    __type__: Literal["passportElements"] = "passportElements"

    elements: list[PassportElement]
    """Telegram Passport elements"""
