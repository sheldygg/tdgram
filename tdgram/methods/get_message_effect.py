from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageEffect
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageEffect(BaseMethod):
    """
    Returns information about a message effect. Returns a 404 error if the effect is not found
    """

    __type__: Literal["getMessageEffect"] = "getMessageEffect"
    __returning_type__ = MessageEffect

    effect_id: int
    """Unique identifier of the effect"""
