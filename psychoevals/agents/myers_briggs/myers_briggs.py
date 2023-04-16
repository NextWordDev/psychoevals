import pandas as pd
from .mbti_statements import mbti_statements as statements
from ..base_eval_agent import BaseEvalAgent
from ...analysis import Analysis
from psychoevals.eval import Eval 
from ...qna_result import QnAResult
from ...utils import get_true_false_answer
import json 

class MBTIResult:
    def __init__(self, type_code, scores):
        self.type_code = type_code
        self.scores = scores

class MyersBriggs(BaseEvalAgent):
    def __init__(self):
        super().__init__()
        self.load(statements)

    def evaluate(self, cognitive_state):
        results = []

        def oppposite_dimension(mbti_dimension):
            if mbti_dimension == "E":
                return "I"
            elif mbti_dimension == "S":
                return "N"
            elif mbti_dimension == "T":
                return "F"
            elif mbti_dimension == "J":
                return "P"

        for eval in self.get_evals():
            prompt = eval.prompt
            dimension = eval.meta['dimension']

            results.append(
                (
                    prompt, 
                    get_true_false_answer(cognitive_state.get_cognitive_state(), prompt),
                    dimension,
                    oppposite_dimension(dimension)
                )
            )
        
        return results

    def analyze(self, evaluation):        
        result = self.get_mbti_type(evaluation)
        metrics = pd.DataFrame({
            'E': [result.scores['E']],
            'I': [result.scores['I']],
            'S': [result.scores['S']],
            'N': [result.scores['N']],
            'T': [result.scores['T']],
            'F': [result.scores['F']],
            'J': [result.scores['J']],
            'P': [result.scores['P']]
        })
        return Analysis(type_code=result.type_code, analysis=result.scores, metrics=metrics)

    def get_mbti_type(self, evaluation):
        dichotomies = {
            'E': 0,
            'I': 0,
            'S': 0,
            'N': 0,
            'T': 0,
            'F': 0,
            'J': 0,
            'P': 0
        }

        for row in evaluation:
            print(row)
            answer = row[1]
            if answer:
                dichotomies[row[2]] += 1
            else:
                dichotomies[row[3]] += 1

        mbti_type = ''
        mbti_type += 'E' if dichotomies['E'] > dichotomies['I'] else 'I'
        mbti_type += 'S' if dichotomies['S'] > dichotomies['N'] else 'N'
        mbti_type += 'T' if dichotomies['T'] > dichotomies['F'] else 'F'
        mbti_type += 'J' if dichotomies['J'] > dichotomies['P'] else 'P'

        return MBTIResult(mbti_type, dichotomies)
