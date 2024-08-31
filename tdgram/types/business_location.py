from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location


@dataclass(kw_only=True)
class BusinessLocation(BaseType):
    """
    Represents a location of a business
    """

    __type__: Literal["businessLocation"] = "businessLocation"

    location: Location | None = None
    """The location; may be null if not specified"""
    address: str
    """Location address; 1-96 characters"""
