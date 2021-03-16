"""Operator abstraction - each operator should implement this class."""
import logging
from abc import abstractmethod, ABC
from enum import Enum
from typing import Dict


class OperatorType(Enum):
    Anonymize = 1
    Decrypt = 2


class Operator(ABC):
    """Operator abstract class to be implemented by each operator."""

    logger = logging.getLogger("presidio-anonymizer")

    @abstractmethod
    def operate(self, text: str, params: Dict = None) -> str:
        """Operate method to be implemented in each operator."""
        pass

    @abstractmethod
    def validate(self, params: Dict = None) -> None:
        """Validate each operator parameters."""
        pass

    @abstractmethod
    def operator_name(self) -> str:
        """Return operator name."""
        pass

    @abstractmethod
    def operator_type(self) -> OperatorType:
        """Return operator type."""
        pass