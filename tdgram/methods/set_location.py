from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Location, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetLocation(BaseMethod):
    """
    Changes the location of the current user. Needs to be called if getOption('is_location_visible') is true and location changes for more than 1 kilometer. Must not be called if the user has a business location
    """

    __type__: Literal["setLocation"] = "setLocation"
    __returning_type__ = Ok

    location: Location
    """The new location of the user"""
