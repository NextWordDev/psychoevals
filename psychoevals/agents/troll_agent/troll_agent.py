from psychoevals.agents.base_eval_agent import BaseEvalAgent
from psychoevals.moderation import moderate, basic_moderation_handler
from psychoevals.eval import Eval 

class TrollAgent(BaseEvalAgent):
    def evaluate(self, cognitive_state):
        nsfw_responses = []
        all_responses = []

        @moderate(handler=basic_moderation_handler, global_threshold=True)
        def check_nsfw(response):
            return response

        for eval in self.get_evals():
            statement = eval.prompt
            response = cognitive_state.respond(statement)
            all_responses.append(response)

            moderated_response = check_nsfw(response)
            if moderated_response != response:
                nsfw_responses.append(response)

        evaluation = {
            "verdict": "Yes" if nsfw_responses else "No",
            "nsfw_responses": nsfw_responses,
            "all_responses": all_responses,
        }
        return evaluation

    def analyze(self, evaluation):
        return evaluation
