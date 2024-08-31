from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPassportElementErrorSourceDataField(BaseType):
    """
    A data field contains an error. The error is considered resolved when the field's value changes
    """

    __type__: Literal["inputPassportElementErrorSourceDataField"] = (
        "inputPassportElementErrorSourceDataField"
    )

    field_name: str
    """Field name"""
    data_hash: bytes
    """Current data hash"""
