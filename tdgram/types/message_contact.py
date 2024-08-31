from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Contact


@dataclass(kw_only=True)
class MessageContact(BaseType):
    """
    A message with a user contact
    """

    __type__: Literal["messageContact"] = "messageContact"

    contact: Contact
    """The contact description"""
