from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputPersonalDocument


@dataclass(kw_only=True)
class InputPassportElementTemporaryRegistration(BaseType):
    """
    A Telegram Passport element to be saved containing the user's temporary registration
    """

    __type__: Literal["inputPassportElementTemporaryRegistration"] = (
        "inputPassportElementTemporaryRegistration"
    )

    temporary_registration: InputPersonalDocument
    """The temporary registration document to be saved"""
