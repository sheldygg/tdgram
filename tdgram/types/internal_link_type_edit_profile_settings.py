from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeEditProfileSettings(BaseType):
    """
    The link is a link to the edit profile section of the application settings
    """

    __type__: Literal["internalLinkTypeEditProfileSettings"] = (
        "internalLinkTypeEditProfileSettings"
    )
