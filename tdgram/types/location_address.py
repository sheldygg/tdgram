from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LocationAddress(BaseType):
    """
    Describes an address of a location
    """

    __type__: Literal["locationAddress"] = "locationAddress"

    country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code"""
    state: str
    """State, if applicable; empty if unknown"""
    city: str
    """City; empty if unknown"""
    street: str
    """The address; empty if unknown"""
