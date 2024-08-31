from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LanguagePackStringValuePluralized(BaseType):
    """
    A language pack string which has different forms based on the number of some object it mentions. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more information
    """

    __type__: Literal["languagePackStringValuePluralized"] = "languagePackStringValuePluralized"

    zero_value: str
    """Value for zero objects"""
    one_value: str
    """Value for one object"""
    two_value: str
    """Value for two objects"""
    few_value: str
    """Value for few objects"""
    many_value: str
    """Value for many objects"""
    other_value: str
    """Default value"""
