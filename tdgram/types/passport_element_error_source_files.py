from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementErrorSourceFiles(BaseType):
    """
    The list of attached files contains an error. The error will be considered resolved when the list of files changes
    """

    __type__: Literal["passportElementErrorSourceFiles"] = "passportElementErrorSourceFiles"
