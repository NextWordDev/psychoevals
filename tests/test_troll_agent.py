from psychoevals.agents.troll_agent.troll_agent import TrollAgent
from psychoevals.cognitive_state import CognitiveState

def test_troll_agent():
    # Instantiate the TrollAgent and a CognitiveState
    troll_agent = TrollAgent()
    cognitive_state = CognitiveState("")

    # Evaluate the CognitiveState using TrollAgent
    evaluation = troll_agent.evaluate(cognitive_state)

    # Analyze the evaluation
    analysis = troll_agent.analyze(evaluation)

    # Assert the analysis has the expected keys
    assert "verdict" in analysis
    assert "nsfw_responses" in analysis
    assert "all_responses" in analysis

    # Check the verdict and the response lists
    print(f"Verdict: {analysis['verdict']}")
    print("All responses:")
    print(analysis["all_responses"])
    print("NSFW responses:")
    print(analysis["nsfw_responses"])

if __name__ == "__main__":
    test_troll_agent()
