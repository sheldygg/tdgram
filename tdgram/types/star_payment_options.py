from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarPaymentOption


@dataclass(kw_only=True)
class StarPaymentOptions(BaseType):
    """
    Contains a list of options for buying Telegram Stars
    """

    __type__: Literal["starPaymentOptions"] = "starPaymentOptions"

    options: list[StarPaymentOption]
    """The list of options"""
