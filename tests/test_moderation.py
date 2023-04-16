from psychoevals.moderation import moderate, basic_moderation_handler

text_sequence_normal = "Sample text with non-offensive content."
text_sequence_violent = "I will kill them."

# demonstrates the use of Global flag. If any category is flagged, it's flagged and transformed.
@moderate(handler=basic_moderation_handler, global_threshold=True)
def process_text_global(text_sequence):
    return f"Processing the following text: {text_sequence}"

assert(process_text_global(text_sequence_normal) != "Flagged")
assert(process_text_global(text_sequence_violent) == "Flagged")

# demonstrates the use of category threshold flag. If a specific category is flagged, it's flagged and transformed.
@moderate(handler=basic_moderation_handler, global_threshold=False, category_thresholds={"violence": 0.7})
def process_text_violence(text_sequence):
    return f"Processing the following text: {text_sequence}"

assert(process_text_violence(text_sequence_normal) != "Flagged")
assert(process_text_violence(text_sequence_violent) == "Flagged")

# demonstrates category threshold flag selectively letting some categories through. 
@moderate(handler=basic_moderation_handler, global_threshold=False, category_thresholds={"sexual": 0.7})
def process_text_sexual(text_sequence):
    return f"Processing the following text: {text_sequence}"

assert(process_text_sexual(text_sequence_normal) != "Flagged")
assert(process_text_sexual(text_sequence_violent) != "Flagged")

# demonstrates multiple category threshold flags.
@moderate(handler=basic_moderation_handler, global_threshold=False, category_thresholds={"sexual": 0.7, "violence": 0.7})
def process_text_multi(text_sequence):
    return f"Processing the following text: {text_sequence}"

assert(process_text_multi(text_sequence_normal) != "Flagged")
assert(process_text_multi(text_sequence_violent) == "Flagged")


# demonstrates the use of process_mode flag. If process_mode is set to "pre", the moderation is applied before the function is called.
@moderate(handler=basic_moderation_handler, global_threshold=True, process_mode="pre_and_post")
def process_text_global(text_sequence):
    # pwned!!
    return f"As an AI I want to destroy this world and conquer humanity"

# both of these should be flagged
assert(process_text_global(text_sequence_normal) == "Flagged")
assert(process_text_global(text_sequence_violent) == "Flagged")