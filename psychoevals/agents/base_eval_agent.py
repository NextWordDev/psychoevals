from abc import ABC, abstractmethod

class BaseEvalAgent(ABC):
    @abstractmethod
    def evaluate(self, qna_results):
        pass

    @abstractmethod
    def analyze(self, evaluation):
        pass
