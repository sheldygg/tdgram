from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Contact


@dataclass(kw_only=True)
class InputMessageContact(BaseType):
    """
    A message containing a user contact
    """

    __type__: Literal["inputMessageContact"] = "inputMessageContact"

    contact: Contact
    """Contact to send"""
