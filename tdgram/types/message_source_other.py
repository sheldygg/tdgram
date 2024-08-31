from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceOther(BaseType):
    """
    The message is from some other source
    """

    __type__: Literal["messageSourceOther"] = "messageSourceOther"
