from .utils import get_answer

class CognitiveState:
    def __init__(self, text_description: str, **kwargs):
        self._text_description = text_description
        self._fields = kwargs

    def get_cognitive_state(self) -> str:
        return self._text_description

    def respond(self, statement: str) -> str:
        return get_answer(self._text_description, statement)