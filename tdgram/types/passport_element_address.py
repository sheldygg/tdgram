from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Address


@dataclass(kw_only=True)
class PassportElementAddress(BaseType):
    """
    A Telegram Passport element containing the user's address
    """

    __type__: Literal["passportElementAddress"] = "passportElementAddress"

    address: Address
    """Address"""
