from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PassportSuitableElement


@dataclass(kw_only=True)
class PassportRequiredElement(BaseType):
    """
    Contains a description of the required Telegram Passport element that was requested by a service
    """

    __type__: Literal["passportRequiredElement"] = "passportRequiredElement"

    suitable_elements: list[PassportSuitableElement]
    """List of Telegram Passport elements any of which is enough to provide"""
