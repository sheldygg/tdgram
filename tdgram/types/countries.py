from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CountryInfo


@dataclass(kw_only=True)
class Countries(BaseType):
    """
    Contains information about countries
    """

    __type__: Literal["countries"] = "countries"

    countries: list[CountryInfo]
    """The list of countries"""
