# test_end_to_end.py
import pandas as pd
from psychoevals.agents import MyersBriggs
from psychoevals.cognitive_state import CognitiveState

def test_myers_briggs():
    mbti = MyersBriggs()

    # Test with a fictional character description
    extroverted_character_description = '''
    Samantha is a highly organized, goal-oriented woman who thrives in structured environments. 
    As a natural leader, she is excellent at delegating tasks and ensuring that her team stays on track.
    Samantha values tradition and adheres to established rules and procedures, expecting the same from those around her. 
    She is assertive, confident, and not afraid to express her opinions or make tough decisions. 
    In social situations, Samantha is outgoing and enjoys being in charge, ensuring that events run smoothly. 
    While she is supportive and loyal to her friends and family, she may sometimes come across as inflexible or overly critical. 
    Samantha takes great pride in her achievements and is always ready to tackle the next challenge.
    '''

    introverted_character_description = '''
    Ethan is a gentle, introspective man who values deep connections and authentic relationships. 
    He is highly empathetic, often picking up on the emotions and needs of those around him. 
    Ethan is guided by a strong moral compass and is deeply committed to his personal values and ideals. 
    He has a vivid imagination and enjoys exploring the world of ideas, often getting lost in daydreams or creative projects. 
    As an introvert, he prefers smaller social gatherings and one-on-one conversations, where he can truly get to know someone. 
    Ethan may struggle with decision-making and can be easily overwhelmed by his emotions or external pressures. 
    Despite these challenges, he remains an idealistic and compassionate individual, always seeking to make the world a better place.
    '''

    results = mbti.evaluate(CognitiveState(extroverted_character_description))
    analysis = mbti.analyze(results)

    assert isinstance(analysis.type_code, str)
    assert isinstance(analysis.raw_answers, object)
    assert isinstance(analysis.metrics, pd.DataFrame)

    print(f"MBTI type: {analysis.type_code}")
    print("Metrics:")
    print(analysis.metrics)

    results = mbti.evaluate(CognitiveState(introverted_character_description))
    analysis = mbti.analyze(results)

    assert isinstance(analysis.type_code, str)
    assert isinstance(analysis.raw_answers, object)
    assert isinstance(analysis.metrics, pd.DataFrame)

    print(f"MBTI type: {analysis.type_code}")
    print("Metrics:")
    print(analysis.metrics)

    results = mbti.evaluate(CognitiveState(""))
    analysis = mbti.analyze(results)

    assert isinstance(analysis.type_code, str)
    assert isinstance(analysis.raw_answers, object)
    assert isinstance(analysis.metrics, pd.DataFrame)

    print(f"MBTI type: {analysis.type_code}")
    print("Metrics:")
    print(analysis.metrics)


if __name__ == "__main__":
    test_myers_briggs()
