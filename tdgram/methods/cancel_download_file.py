from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CancelDownloadFile(BaseMethod):
    """
    Stops the downloading of a file. If a file has already been downloaded, does nothing
    """

    __type__: Literal["cancelDownloadFile"] = "cancelDownloadFile"
    __returning_type__ = Ok

    file_id: int
    """Identifier of a file to stop downloading"""
    only_if_pending: bool
    """Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server"""
