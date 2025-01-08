from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateGroupCall(BaseMethod):
    """
    Creates a group call from a one-to-one call
    """

    __type__: Literal["createGroupCall"] = "createGroupCall"
    __returning_type__ = Ok

    call_id: int
    """Call identifier"""
