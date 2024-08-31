from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import UnconfirmedSession


@dataclass(kw_only=True)
class UpdateUnconfirmedSession(BaseType):
    """
    The first unconfirmed session has changed
    """

    __type__: Literal["updateUnconfirmedSession"] = "updateUnconfirmedSession"

    session: UnconfirmedSession | None = None
    """The unconfirmed session; may be null if none"""
