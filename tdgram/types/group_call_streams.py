from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GroupCallStream


@dataclass(kw_only=True)
class GroupCallStreams(BaseType):
    """
    Represents a list of group call streams
    """

    __type__: Literal["groupCallStreams"] = "groupCallStreams"

    streams: list[GroupCallStream]
    """A list of group call streams"""
