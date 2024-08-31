from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateAvailableMessageEffects(BaseType):
    """
    The list of available message effects has changed
    """

    __type__: Literal["updateAvailableMessageEffects"] = "updateAvailableMessageEffects"

    reaction_effect_ids: list[int]
    """The new list of available message effects from emoji reactions"""
    sticker_effect_ids: list[int]
    """The new list of available message effects from Premium stickers"""
