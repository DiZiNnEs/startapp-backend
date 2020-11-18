from abc import ABC, abstractmethod


class ClothesHandlerInterface(ABC):
    def __init__(self, temperature: int) -> None:
        self._TEMPERATURE = temperature

    def get_recommendation(self, recommendation: dict) -> str:
        return self._handle_recommendation(recommendation)

    @abstractmethod
    def _handle_recommendation(self, recommendation: dict) -> str:
        raise NotImplementedError
