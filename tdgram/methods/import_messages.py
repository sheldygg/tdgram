from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ImportMessages(BaseMethod):
    """
    Imports messages exported from another app
    """

    __type__: Literal["importMessages"] = "importMessages"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info member right"""
    message_file: InputFile
    """File with messages to import. Only inputFileLocal and inputFileGenerated are supported. The file must not be previously uploaded"""
    attached_files: list[InputFile]
    """Files used in the imported messages. Only inputFileLocal and inputFileGenerated are supported. The files must not be previously uploaded"""
