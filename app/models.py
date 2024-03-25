from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Unbabel/gec-t5_small")
model = AutoModelForSeq2SeqLM.from_pretrained("Unbabel/gec-t5_small")


def correct_text(input_text: str) -> str:
    tokenized_sentence = tokenizer.encode(
        "gec: " + input_text,
        max_length=128,
        truncation=True,
        padding="max_length",
        return_tensors="pt",
    )

    outputs = model.generate(
        tokenized_sentence,
        max_length=128,
        num_beams=5,
        early_stopping=True,
    )

    corrected_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    )

    return corrected_text
