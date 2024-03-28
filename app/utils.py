from app.config import Config
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_PATH)


def check_input_length(input_text: str) -> bool:
    """
    Tokenizes the input text and checks if it exceeds the maximum token length.

    Args:
        input_text (str): The input text to be checked.

    Returns:
        bool: True if input text is within the allowable length, False otherwise.
    """
    max_length = Config.MAX_LENGTH

    tokenized_input = tokenizer(
        "gec: " + input_text,
        return_tensors="pt",
        truncation=False,
        padding=False,
    ).input_ids

    return len(tokenized_input[0]) <= max_length
