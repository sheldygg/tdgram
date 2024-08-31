from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeChangePhoneNumber(BaseType):
    """
    The link is a link to the change phone number section of the application
    """

    __type__: Literal["internalLinkTypeChangePhoneNumber"] = "internalLinkTypeChangePhoneNumber"
