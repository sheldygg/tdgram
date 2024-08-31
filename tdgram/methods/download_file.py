from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import File
from .base import BaseMethod


@dataclass(kw_only=True)
class DownloadFile(BaseMethod):
    """
    Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates
    """

    __type__: Literal["downloadFile"] = "downloadFile"
    __returning_type__ = File

    file_id: int
    """Identifier of the file to download"""
    priority: int
    """Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first"""
    offset: int
    """The starting position from which the file needs to be downloaded"""
    limit: int
    """Number of bytes which need to be downloaded starting from the 'offset' position before the download will automatically be canceled; use 0 to download without a limit"""
    synchronous: bool
    """Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started"""
