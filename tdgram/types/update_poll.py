from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Poll


@dataclass(kw_only=True)
class UpdatePoll(BaseType):
    """
    A poll was updated; for bots only
    """

    __type__: Literal["updatePoll"] = "updatePoll"

    poll: Poll
    """New data about the poll"""
