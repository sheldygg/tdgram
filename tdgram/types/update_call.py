from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Call


@dataclass(kw_only=True)
class UpdateCall(BaseType):
    """
    New call was created or information about a call was updated
    """

    __type__: Literal["updateCall"] = "updateCall"

    call: Call
    """New data about a call"""
