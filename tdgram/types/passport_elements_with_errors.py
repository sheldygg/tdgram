from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PassportElement, PassportElementError


@dataclass(kw_only=True)
class PassportElementsWithErrors(BaseType):
    """
    Contains information about a Telegram Passport elements and corresponding errors
    """

    __type__: Literal["passportElementsWithErrors"] = "passportElementsWithErrors"

    elements: list[PassportElement]
    """Telegram Passport elements"""
    errors: list[PassportElementError]
    """Errors in the elements that are already available"""
