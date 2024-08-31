from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputFileRemote(BaseType):
    """
    A file defined by its remote identifier. The remote identifier is guaranteed to be usable only if the corresponding file is still accessible to the user and known to TDLib.
    """

    __type__: Literal["inputFileRemote"] = "inputFileRemote"

    id: str
    """Remote file identifier"""
