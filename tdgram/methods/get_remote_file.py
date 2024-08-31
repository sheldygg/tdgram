from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import File, FileType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRemoteFile(BaseMethod):
    """
    Returns information about a file by its remote identifier; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message. Even the request succeeds, the file can be used only if it is still accessible to the user.
    """

    __type__: Literal["getRemoteFile"] = "getRemoteFile"
    __returning_type__ = File

    remote_file_id: str
    """Remote identifier of the file to get"""
    file_type: FileType | None = None
    """File type; pass null if unknown"""
