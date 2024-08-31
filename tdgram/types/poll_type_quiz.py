from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class PollTypeQuiz(BaseType):
    """
    A poll in quiz mode, which has exactly one correct answer option and can be answered only once
    """

    __type__: Literal["pollTypeQuiz"] = "pollTypeQuiz"

    correct_option_id: int
    """0-based identifier of the correct answer option; -1 for a yet unanswered poll"""
    explanation: FormattedText
    """Text that is shown when the user chooses an incorrect answer or taps on the lamp icon; 0-200 characters with at most 2 line feeds; empty for a yet unanswered poll"""
