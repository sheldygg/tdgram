from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StatisticalValue(BaseType):
    """
    A value with information about its recent changes
    """

    __type__: Literal["statisticalValue"] = "statisticalValue"

    value: float
    """The current value"""
    previous_value: float
    """The value for the previous day"""
    growth_rate_percentage: float
    """The growth rate of the value, as a percentage"""
