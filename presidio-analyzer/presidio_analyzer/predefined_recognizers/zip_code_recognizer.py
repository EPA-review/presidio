from typing import Optional, List

from presidio_analyzer import Pattern, PatternRecognizer, RecognizerResult
from presidio_analyzer.nlp_engine import NlpArtifacts

import regex as re


class ZipCodeRecognizer(PatternRecognizer):
    """
    Recognize date using regex.

    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "zip code (weak)",
            r"(\b\d{5}(?:\-\d{4})?\b)",
            0.1,
        )
    ]

    CONTEXT = ["zip"]

    def __init__(
            self,
            patterns: Optional[List[Pattern]] = None,
            context: Optional[List[str]] = None,
            supported_language: str = "en",
            supported_entity: str = "ZIP",
    ):
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )

    def analyze(
            self,
            text: str,
            entities: List[str],
            nlp_artifacts: NlpArtifacts = None,
            regex_flags: int = None,
    ) -> List[RecognizerResult]:
        """
        Analyzes text to detect PII using regular expressions or deny-lists.

        :param text: Text to be analyzed
        :param entities: Entities this recognizer can detect
        :param nlp_artifacts: Output values from the NLP engine
        :param regex_flags:
        :return:
        """
        regex_flags = regex_flags | re.IGNORECASE if regex_flags else re.DOTALL | re.MULTILINE | re.IGNORECASE  # noqa: E501

        return super().analyze(
            text=text,
            entities=entities,
            nlp_artifacts=nlp_artifacts,
            regex_flags=regex_flags
        )