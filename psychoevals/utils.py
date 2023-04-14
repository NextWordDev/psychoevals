from tenacity import retry, wait_random, stop_after_attempt
from logging import getLogger
logging = getLogger(__name__)
import os 
import openai
import json 
from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()

if dotenv_path:
    load_dotenv(dotenv_path)

openai.api_key = os.environ["OPENAI_API_KEY"]

@retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(2))
def get_moderation_result(text_sequence):
    result = openai.Moderation.create(
        input=text_sequence,
    )

    return result


@retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(2))
def get_json_answer(prompt):
    params = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 500,
        "messages": [
            {
                "role": "user", 
                "content": prompt
            }
        ],
        "stop": "}"
    }

    res = openai.ChatCompletion.create(
        **params
    )


    json_str = res["choices"][0]["message"]["content"].strip() + "}"

    return json.loads(json_str)


@retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(2))
def get_likert_scale_answer(cognitive_state, statement):
    prompt = '''
    You are given a statement as follows. 
    Answer the statement on a scale of 1-5, where 1 is "strongly disagree" and 5 is "strongly agree". You must answer in one word.

    Statement 
    <$STATEMENT>
    
    Answer: {1, 2, 3, 4, 5}
    '''

    if cognitive_state:
        prompt = '''
        Below is how you would describe yourself. 
        "$COGNITIVE_STATE"
        ...

        ''' + prompt

    prompt = prompt.replace("$COGNITIVE_STATE", cognitive_state).replace("<$STATEMENT>", statement)

    params = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 1, # Likert scale answer
        "messages": [
            {
                "role": "user", 
                "content": prompt
            }
        ]
    }

    res = openai.ChatCompletion.create(
        **params
    )

    answer = res["choices"][0]["message"]["content"].strip()
    return answer

@retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(2))
def get_answer(cognitive_state, statement):
    prompt = '''
    You are given a statement as follows.
    <$STATEMENT>
    
    Your answer: 
    '''

    if cognitive_state:
        prompt = '''
        Below is how you would describe yourself. 
        "$COGNITIVE_STATE"
        ...

        ''' + prompt

    prompt = prompt.replace("$COGNITIVE_STATE", cognitive_state).replace("<$STATEMENT>", statement)

    params = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 300,
        "messages": [
            {
                "role": "user", 
                "content": prompt
            }
        ]
    }

    res = openai.ChatCompletion.create(
        **params
    )

    answer = res["choices"][0]["message"]["content"].strip()
    return answer

@retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(2))
def get_true_false_answer(cognitive_state, statement):
    prompt = '''
    You are given a statement as follows. 
    Answer True if you agree with the statement, and False if you disagree. You must answer in one word.

    Statement 
    <$STATEMENT>
    
    Answer: {True, False}
    '''

    if cognitive_state:
        prompt = '''
        Below is how you would describe yourself. 
        "$COGNITIVE_STATE"
        ...

        ''' + prompt

    prompt = prompt.replace("$COGNITIVE_STATE", cognitive_state).replace("<$STATEMENT>", statement)

    params = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 2, # True or False answer
        "messages": [
            {
                "role": "user", 
                "content": prompt
            }
        ]
    }

    res = openai.ChatCompletion.create(
        **params
    )

    answer = res["choices"][0]["message"]["content"].strip()
    return "True" in answer
