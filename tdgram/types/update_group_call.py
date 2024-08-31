from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GroupCall


@dataclass(kw_only=True)
class UpdateGroupCall(BaseType):
    """
    Information about a group call was updated
    """

    __type__: Literal["updateGroupCall"] = "updateGroupCall"

    group_call: GroupCall
    """New data about a group call"""
