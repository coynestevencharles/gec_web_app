from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.config import Config

tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(Config.MODEL_PATH)


def correct_text(input_text: str) -> str:
    """
    Corrects the input text using the GEC model.

    Args:
        input_text (str): The input text to be corrected.

    Returns:
        corrected_text (str): The corrected text.
    """
    tokenized_sentence = tokenizer.encode(
        Config.INPUT_PREFIX + input_text,
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
