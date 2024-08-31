from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StoryContentUnsupported(BaseType):
    """
    A story content that is not supported in the current TDLib version
    """

    __type__: Literal["storyContentUnsupported"] = "storyContentUnsupported"
