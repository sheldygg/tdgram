from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CollectibleItemTypePhoneNumber(BaseType):
    """
    A phone number
    """

    __type__: Literal["collectibleItemTypePhoneNumber"] = "collectibleItemTypePhoneNumber"

    phone_number: str
    """The phone number"""
