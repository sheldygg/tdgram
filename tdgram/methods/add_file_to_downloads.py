from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import File
from .base import BaseMethod


@dataclass(kw_only=True)
class AddFileToDownloads(BaseMethod):
    """
    Adds a file from a message to the list of file downloads. Download progress and completion of the download will be notified through updateFile updates.
    """

    __type__: Literal["addFileToDownloads"] = "addFileToDownloads"
    __returning_type__ = File

    file_id: int
    """Identifier of the file to download"""
    chat_id: int
    """Chat identifier of the message with the file"""
    message_id: int
    """Message identifier"""
    priority: int
    """Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first"""
