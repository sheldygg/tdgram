from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LanguagePackStringValueDeleted(BaseType):
    """
    A deleted language pack string, the value must be taken from the built-in English language pack
    """

    __type__: Literal["languagePackStringValueDeleted"] = "languagePackStringValueDeleted"
