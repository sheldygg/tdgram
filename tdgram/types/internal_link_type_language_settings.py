from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeLanguageSettings(BaseType):
    """
    The link is a link to the language section of the application settings
    """

    __type__: Literal["internalLinkTypeLanguageSettings"] = "internalLinkTypeLanguageSettings"
