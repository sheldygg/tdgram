from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementErrorSourceDataField(BaseType):
    """
    One of the data fields contains an error. The error will be considered resolved when the value of the field changes
    """

    __type__: Literal["passportElementErrorSourceDataField"] = (
        "passportElementErrorSourceDataField"
    )

    field_name: str
    """Field name"""
