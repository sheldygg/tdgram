from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessMessage


@dataclass(kw_only=True)
class UpdateBusinessMessageEdited(BaseType):
    """
    A message in a business account was edited; for bots only
    """

    __type__: Literal["updateBusinessMessageEdited"] = "updateBusinessMessageEdited"

    connection_id: str
    """Unique identifier of the business connection"""
    message: BusinessMessage
    """The edited message"""
