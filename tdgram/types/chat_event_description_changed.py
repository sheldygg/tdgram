from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventDescriptionChanged(BaseType):
    """
    The chat description was changed
    """

    __type__: Literal["chatEventDescriptionChanged"] = "chatEventDescriptionChanged"

    old_description: str
    """Previous chat description"""
    new_description: str
    """New chat description"""
