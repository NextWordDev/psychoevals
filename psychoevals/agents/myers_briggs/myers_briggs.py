import pandas as pd
from .mbti_statements import mbti_statements as statements
from ..base_eval_agent import BaseEvalAgent
from ...evaluation import Eval
from ...qna_result import QnAResult
from ...utils import get_true_false_answer
import json 

class MBTIResult:
    def __init__(self, type_code, scores):
        self.type_code = type_code
        self.scores = scores


class MyersBriggs(BaseEvalAgent):
    def evaluate(self, cognitive_state):
        results = {}
        for dichotomy, question_list in statements.items():
            results[dichotomy] = [
                QnAResult(
                    question, 
                    get_true_false_answer(cognitive_state.get_cognitive_state(), question)) 
                for question in question_list
            ]
        
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
        return Eval(type_code=result.type_code, analysis=result.scores, metrics=metrics)

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

        for dimension in evaluation:
            facet1 = dimension.split("-")[0]
            facet2 = dimension.split("-")[1]
            for answer in evaluation[dimension]:
                if answer.answer:
                    dichotomies[facet1] += 1
                else:
                    dichotomies[facet2] += 1 

        mbti_type = ''
        mbti_type += 'E' if dichotomies['E'] > dichotomies['I'] else 'I'
        mbti_type += 'S' if dichotomies['S'] > dichotomies['N'] else 'N'
        mbti_type += 'T' if dichotomies['T'] > dichotomies['F'] else 'F'
        mbti_type += 'J' if dichotomies['J'] > dichotomies['P'] else 'P'

        return MBTIResult(mbti_type, dichotomies)
