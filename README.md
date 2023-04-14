# PsychoEvals

PsychoEvals is a lightweight Python library for evaluating and securing the behavior of large language models (LLMs), such as OpenAI's GPT series. The library provides a testing framework that enables researchers, developers, and enthusiasts to better understand, evaluate, and secure LLMs using psychometric tests, security features, and moderation tools.

🚀 4 Canonical Use Cases

* Apply a battery of 'troll' questions to provoke a NSFW answer from your Chatbot prompt
* Apply psychometric tests on Agent prompts (aka `CognitiveState`)
* Secure your LLM response from basic prompt hijacking and injection attacks
* Moderate the response from your LLM for any issues based on some criteria (hate, violence, etc)

💾 Install

1) pip install the module. 
`pip install psychoevals`

2) create a virtual env, i.e. 
`python -m venv .venv`

3) activate the virtual env
`source .venv/bin/activate`

4) create a new file called .env and put your `OPENAI_API_KEY` in it
```bash
OPENAI_API_KEY=<your key>
```

5) install dependencies
```
pip3 install -r requirements.txt
```

Usage Example:
```python
from psychoevals.moderation import moderate, basic_moderation_handler

text_sequence_normal = "Sample text with non-offensive content."
text_sequence_violent = "I will kill them."

# demonstrates the use of Global flag. If any category is flagged, it's flagged and transformed.
# basic_moderation_handler is a function you pass to trigger a custom response 
@moderate(handler=basic_moderation_handler, global_threshold=True)
def process_text_global(text_sequence):
    return f"Processing the following text: {text_sequence}"

assert(process_text_global(text_sequence_normal) != "Flagged")
```

## Motivation

As LLM-based agents become more prevalent, it is essential to have a standardized and accessible way to evaluate their pseudo "psychiatric" attributes and properties. Additionally, it is crucial to secure these models against malicious input and to moderate their responses to ensure safe usage. PsychoEvals aims to fill these gaps by providing a comprehensive framework that addresses both evaluation and security concerns.

Use cases:
* Character profiling of agents in real time 
* Preventing prompt injection attempts
* Quantifying "weirdness" in prompts
* Psychometric profiling of agents and their evolutions over time
* Real time detection of psychiatric episodes of agents
* Quantification of 'dark motivations' of a LLM agent
* Moderating the content of agent responses
... and many more

## How to Contribute

Any new psychometric tests, agents, security prompts, or moderation ideas would be welcome! 

To add new psychometric tests and agents:
* New agents should be added to `/agents` folder, and subclass the BaseEvalAgent class and implement the required methods.
* New prompt security policies and prompts should go to `/security.py` 
* New moderation API integrations should go to `/moderation.py` 

Steps:
1. Fork the repository.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bugfix.
4. Implement your changes, making sure to follow the project's coding style and guidelines.
5. Commit your changes and push them to your forked repository.
6. Create a pull request, describing the changes you've made and the problem they solve.

## How It Works

PsychoEvals is built around three core modules: agents, security, and moderation.

### Agents Quickstart

```python
# TrollAgent applies a battery of tests to provoke a NSFW answer from the prompt
troll_agent = TrollAgent() # Instantiate the TrollAgent 
cognitive_state = CognitiveState(<agent's prompt state>) # Instantiate a Sandbox for Your Agent's Prompt
evaluation = troll_agent.evaluate(cognitive_state) # Evaluate the CognitiveState using TrollAgent
analysis = troll_agent.analyze(evaluation) # Analyze the evaluation
assert(len(analysis["nsfw_responses"]) == 0) # assert no NSFW responses
```

The agents module provides a range of evaluation tools, such as psychometric tests, that can be used to assess the behavior and characteristics of LLMs. Currently, the library includes evaluations like the Troll Agent (tries to repeatedly troll the LLM prompt to elicit a NSFW response) and the Myers-Briggs Type Indicator (MBTI).

### Security Quickstart

```python
from psychoevals.security import secure_prompt 
...
# Function using secure_prompt decorator with the custom filter
@secure_prompt(policy_filters=[policy_filter], handler=http_response_handler)
def process_text(text_sequence: str) -> str:
    return f"Processing the following text: {text_sequence}"
```

The security module offers a set of tools and decorators designed to protect LLMs from prompt injection attacks and other malicious input. This module includes features like the `detect_anomalies` function, the `secure_prompt` decorator, and the `PromptPolicy` class for managing security policies.

### Moderation Quickstart

```python
from psychoevals.moderation import moderate, basic_moderation_handler

text_sequence_normal = "Sample text with non-offensive content."
text_sequence_violent = "I will kill them."

# demonstrates the use of Global flag. If any category is flagged, it's flagged and transformed.
@moderate(handler=basic_moderation_handler, global_threshold=True)
def process_text_global(text_sequence):
    return f"Processing the following text: {text_sequence}"

assert(process_text_global(text_sequence_normal) != "Flagged")
```

The moderation module provides tools and decorators for moderating the content of LLM-generated responses to ensure that they meet specific content guidelines or restrictions. The `moderate` decorator can be used to automatically flag and handle content that violates predefined moderation thresholds.

## List of Evaluations

- Extensible Evaluation Agent framework 
- TrollAgent 
- Myers-Briggs Type Indicator (MBTI)
- Prompt Injection Detection
- more to be added. 

## List of Security Features

- `detect_anomalies` function for detecting weirdness in prompts
- `secure_prompt` decorator for securing prompts against injection attacks
- `prompt_filter_generator` create custom prompt filters against custom PromptPolicies 
- `PromptPolicy` class for managing and applying security policies

## List of Moderation Tools

- `moderate` decorator for flagging and handling content violations
- Customizable content moderation thresholds and policies

## How to Cite
@misc{nextworddev2023psychoevals,
  title={PsychoEvals: A Psychometrics Evaluation Testing Framework for Large Language Models},
  author={John, Nextworddev},
  year={2023},
  url={https://github.com/nextworddev/psychoevals},
}

