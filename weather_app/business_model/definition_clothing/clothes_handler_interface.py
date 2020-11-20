from abc import ABC, abstractmethod


class ClothesHandlerInterface(ABC):
    def __init__(self, temperature: int) -> None:
        self._TEMPERATURE = temperature

    def get_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        return self._handle_clothes_recommendation(dictionary_recommendations)

    @abstractmethod
    def _handle_clothes_recommendation(self, dictionary_recommendations: dict) -> str:
        raise NotImplementedError
