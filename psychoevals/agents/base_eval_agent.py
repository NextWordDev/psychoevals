from abc import ABC, abstractmethod
from collections import OrderedDict
from psychoevals.eval import Eval
from psychoevals.analysis import Analysis
from typing import List, Callable, Optional, Dict, Any
from psychoevals.cognitive_state import CognitiveState

class BaseEvalAgent(ABC):
    def __init__(self):
        self._evals = OrderedDict()

    def load(self, evals: List):
        for item in evals:
            eval_object = Eval(prompt=item["prompt"], meta=item["meta"])
            self._evals[eval_object._id] = eval_object
        return self 

    def upsert_eval(self, eval_object):
        self._evals[eval_object._id] = eval_object

    def remove_eval(self, eval_id):
        if eval_id in self._evals:
            del self._evals[eval_id]
        else:
            print(f"Eval ID {eval_id} not found in the tests.")

    def get_evals(self):
        for eval_id, eval_object in self._evals.items():
            yield eval_object

    @abstractmethod
    def evaluate(self, cognitive_state: CognitiveState):
        pass

    @abstractmethod
    def analyze(self, analysis: Analysis):
        pass
