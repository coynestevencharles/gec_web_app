from app.models import correct_text
from celery import shared_task


@shared_task(ignore_result=False)
def async_correct_text(input_text):
    try:
        return correct_text(input_text)
    except Exception as e:
        return {"error": "Failed to process the text due to an internal error."}
