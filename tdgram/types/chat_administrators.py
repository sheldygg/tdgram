from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatAdministrator


@dataclass(kw_only=True)
class ChatAdministrators(BaseType):
    """
    Represents a list of chat administrators
    """

    __type__: Literal["chatAdministrators"] = "chatAdministrators"

    administrators: list[ChatAdministrator]
    """A list of chat administrators"""
