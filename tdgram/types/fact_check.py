from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class FactCheck(BaseType):
    """
    Describes a fact-check added to the message by an independent checker
    """

    __type__: Literal["factCheck"] = "factCheck"

    text: FormattedText
    """Text of the fact-check"""
    country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code of the country for which the fact-check is shown"""
