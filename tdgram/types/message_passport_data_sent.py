from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PassportElementType


@dataclass(kw_only=True)
class MessagePassportDataSent(BaseType):
    """
    Telegram Passport data has been sent to a bot
    """

    __type__: Literal["messagePassportDataSent"] = "messagePassportDataSent"

    types: list[PassportElementType]
    """List of Telegram Passport element types sent"""
