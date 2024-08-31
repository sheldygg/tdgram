from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentSuggestProfilePhoto(BaseType):
    """
    A profile photo was suggested to the user
    """

    __type__: Literal["pushMessageContentSuggestProfilePhoto"] = (
        "pushMessageContentSuggestProfilePhoto"
    )
