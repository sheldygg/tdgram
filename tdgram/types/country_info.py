from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CountryInfo(BaseType):
    """
    Contains information about a country
    """

    __type__: Literal["countryInfo"] = "countryInfo"

    country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code"""
    name: str
    """Native name of the country"""
    english_name: str
    """English name of the country"""
    is_hidden: bool
    """True, if the country must be hidden from the list of all countries"""
    calling_codes: list[str]
    """List of country calling codes"""
