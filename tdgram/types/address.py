from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Address(BaseType):
    """
    Describes an address
    """

    __type__: Literal["address"] = "address"

    country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code"""
    state: str
    """State, if applicable"""
    city: str
    """City"""
    street_line1: str
    """First line of the address"""
    street_line2: str
    """Second line of the address"""
    postal_code: str
    """Address postal code"""
