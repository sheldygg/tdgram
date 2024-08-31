from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageAutoDeleteTime
from .base import BaseMethod


@dataclass(kw_only=True)
class GetDefaultMessageAutoDeleteTime(BaseMethod):
    """
    Returns default message auto-delete time setting for new chats
    """

    __type__: Literal["getDefaultMessageAutoDeleteTime"] = "getDefaultMessageAutoDeleteTime"
    __returning_type__ = MessageAutoDeleteTime
