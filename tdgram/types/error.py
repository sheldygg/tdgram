from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Error(BaseType):
    """
    An object of this type can be returned on every function call, in case of an error
    """

    __type__: Literal["error"] = "error"

    code: int
    """Error code; subject to future changes. If the error code is 406, the error message must not be processed in any way and must not be displayed to the user"""
    message: str
    """Error message; subject to future changes"""
