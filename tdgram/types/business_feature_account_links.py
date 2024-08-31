from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureAccountLinks(BaseType):
    """
    The ability to create links to the business account with predefined message text
    """

    __type__: Literal["businessFeatureAccountLinks"] = "businessFeatureAccountLinks"
