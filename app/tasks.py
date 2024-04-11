from app.models import correct_text
from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task(ignore_result=False)
def async_correct_text(input_text):
    try:
        corrected_text = correct_text(input_text)
        logger.info(f"Processed input: {input_text}")
        return corrected_text
    except Exception as e:
        logger.error(
            "Failed to process the text due to an internal error.", exc_info=True
        )
        return {"error": "Failed to process the text due to an internal error."}
