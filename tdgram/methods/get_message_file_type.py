from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageFileType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageFileType(BaseMethod):
    """
    Returns information about a file with messages exported from another application
    """

    __type__: Literal["getMessageFileType"] = "getMessageFileType"
    __returning_type__ = MessageFileType

    message_file_head: str
    """Beginning of the message file; up to 100 first lines"""
