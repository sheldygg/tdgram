from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile


@dataclass(kw_only=True)
class InputChatPhotoAnimation(BaseType):
    """
    An animation in MPEG4 format; must be square, at most 10 seconds long, have width between 160 and 1280 and be at most 2MB in size
    """

    __type__: Literal["inputChatPhotoAnimation"] = "inputChatPhotoAnimation"

    animation: InputFile
    """Animation to be set as profile photo. Only inputFileLocal and inputFileGenerated are allowed"""
    main_frame_timestamp: float
    """Timestamp of the frame, which will be used as static chat photo"""
