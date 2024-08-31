from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeBankCardNumber(BaseType):
    """
    A bank card number. The getBankCardInfo method can be used to get information about the bank card
    """

    __type__: Literal["textEntityTypeBankCardNumber"] = "textEntityTypeBankCardNumber"
