from abc import ABC, abstractmethod


class ClothesInterface(ABC):
    def __init__(self, temperature: int) -> None:
        self._TEMPERATURE = temperature

    def get_recommendation(self) -> str:
        return self._handle_recommendation()

    @abstractmethod
    def _handle_recommendation(self) -> str:
        raise NotImplementedError
