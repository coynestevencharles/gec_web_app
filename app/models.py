from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.config import Config

tokenizer = AutoTokenizer.from_pretrained("Unbabel/gec-t5_small")
model = AutoModelForSeq2SeqLM.from_pretrained("Unbabel/gec-t5_small")


def correct_text(input_text: str) -> str:
    """
    Corrects the input text using the GEC model.

    Args:
        input_text (str): The input text to be corrected.

    Returns:
        corrected_text (str): The corrected text.
    """
    tokenized_sentence = tokenizer.encode(
        "gec: " + input_text,
        max_length=Config.MAX_LENGTH,
        truncation=True,
        padding="max_length",
        return_tensors="pt",
    )

    outputs = model.generate(
        tokenized_sentence,
        max_length=Config.MAX_LENGTH,
        num_beams=5,
        early_stopping=True,
    )

    corrected_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    )

    return corrected_text


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
