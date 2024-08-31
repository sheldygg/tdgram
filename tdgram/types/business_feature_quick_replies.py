from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureQuickReplies(BaseType):
    """
    The ability to use quick replies
    """

    __type__: Literal["businessFeatureQuickReplies"] = "businessFeatureQuickReplies"
