from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanSendStoryResultOk(BaseType):
    """
    A story can be sent
    """

    __type__: Literal["canSendStoryResultOk"] = "canSendStoryResultOk"
