from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PollTypeRegular(BaseType):
    """
    A regular poll
    """

    __type__: Literal["pollTypeRegular"] = "pollTypeRegular"

    allow_multiple_answers: bool
    """True, if multiple answer options can be chosen simultaneously"""
