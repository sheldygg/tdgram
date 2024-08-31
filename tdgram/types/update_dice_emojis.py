from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateDiceEmojis(BaseType):
    """
    The list of supported dice emojis has changed
    """

    __type__: Literal["updateDiceEmojis"] = "updateDiceEmojis"

    emojis: list[str]
    """The new list of supported dice emojis"""
