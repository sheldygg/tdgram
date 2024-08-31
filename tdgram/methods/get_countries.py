from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Countries
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCountries(BaseMethod):
    """
    Returns information about existing countries. Can be called before authorization
    """

    __type__: Literal["getCountries"] = "getCountries"
    __returning_type__ = Countries
