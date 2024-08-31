from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Poll


@dataclass(kw_only=True)
class MessagePoll(BaseType):
    """
    A message with a poll
    """

    __type__: Literal["messagePoll"] = "messagePoll"

    poll: Poll
    """The poll description"""
