from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessMessage


@dataclass(kw_only=True)
class UpdateNewBusinessMessage(BaseType):
    """
    A new message was added to a business account; for bots only
    """

    __type__: Literal["updateNewBusinessMessage"] = "updateNewBusinessMessage"

    connection_id: str
    """Unique identifier of the business connection"""
    message: BusinessMessage
    """The new message"""
