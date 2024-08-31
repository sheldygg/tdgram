from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Address


@dataclass(kw_only=True)
class InputPassportElementAddress(BaseType):
    """
    A Telegram Passport element to be saved containing the user's address
    """

    __type__: Literal["inputPassportElementAddress"] = "inputPassportElementAddress"

    address: Address
    """The address to be saved"""
