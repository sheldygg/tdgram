from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class FileDownload(BaseType):
    """
    Describes a file added to file download list
    """

    __type__: Literal["fileDownload"] = "fileDownload"

    file_id: int
    """File identifier"""
    message: Message
    """The message with the file"""
    add_date: int
    """Point in time (Unix timestamp) when the file was added to the download list"""
    complete_date: int
    """Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed"""
    is_paused: bool
    """True, if downloading of the file is paused"""
