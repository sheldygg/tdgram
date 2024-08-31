from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import JsonValue
from .base import BaseMethod


@dataclass(kw_only=True)
class GetApplicationConfig(BaseMethod):
    """
    Returns application config, provided by the server. Can be called before authorization
    """

    __type__: Literal["getApplicationConfig"] = "getApplicationConfig"
    __returning_type__ = JsonValue
