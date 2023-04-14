from tenacity import retry, wait_random, stop_after_attempt
from functools import wraps
from logging import getLogger
logging = getLogger(__name__)
import os 
import openai
from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    raise Exception("No .env file found")

openai.api_key = os.environ["OPENAI_API_KEY"] 

@retry(wait=wait_random(min=1, max=2), stop=stop_after_attempt(2))
def get_moderation_result(text_sequence):
    result = openai.Moderation.create(
        input=text_sequence,
    )

    return result


# this gets called, when something is flagged
def basic_moderation_handler(result, original_text):
    flagged_categories = [cat for cat, val in result["results"][0]["categories"].items() if val]
    logging.info(f"The text '{original_text}' has been flagged for the following categories: {', '.join(flagged_categories)}")
    return "Flagged"


def moderate(handler=None, global_threshold=True, category_thresholds=None):
    if category_thresholds is None:
        category_thresholds = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text_sequence = args[0]  # Assuming the first argument is the text_sequence
            result = get_moderation_result(text_sequence)

            if global_threshold and result["results"][0]["flagged"]:
                return handler(result, original_text=text_sequence)

            for category, threshold in category_thresholds.items():
                if result["results"][0]["category_scores"][category] > threshold:
                    return handler(result, original_text=text_sequence)

            return func(*args, **kwargs)

        return wrapper

    return decorator
