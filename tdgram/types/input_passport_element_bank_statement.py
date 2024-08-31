from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputPersonalDocument


@dataclass(kw_only=True)
class InputPassportElementBankStatement(BaseType):
    """
    A Telegram Passport element to be saved containing the user's bank statement
    """

    __type__: Literal["inputPassportElementBankStatement"] = "inputPassportElementBankStatement"

    bank_statement: InputPersonalDocument
    """The bank statement to be saved"""
