from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text, ThemeParameters
from .base import BaseMethod


@dataclass(kw_only=True)
class GetThemeParametersJsonString(BaseMethod):
    """
    Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously
    """

    __type__: Literal["getThemeParametersJsonString"] = "getThemeParametersJsonString"
    __returning_type__ = Text

    theme: ThemeParameters
    """Theme parameters to convert to JSON"""
