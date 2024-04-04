# Grammatical Error Correction Web App

A simple web application that accepts input text and corrects it using a natural language processing model.

This is being built from the bottom up as an exercise in model training and deployment.

Planning to implement the following:

* An "error correction" tool that directly fixes input sentences.
* An "error checker" tool that highlights errors for the user's consideration.

Currently, a basic version of the corrector is available, using a sequence-to-sequence model fine-tuned from T5 following the paper "[A Simple Recipe for Multilingual Grammatical Error Correction](https://arxiv.org/abs/2106.03830)." See the [Hugging Face model card](https://huggingface.co/Buntan/gec-t5-v1_1-small) and [training code](https://github.com/coynestevencharles/gec_model_training) for more details.

![Screenshot of the error correction tool](assets/error_correction_ui_screenshot.png?raw=true)

## Setup

```bash
# Install redis if necessary, e.g.,
brew install redis

# Create an environment for this project, e.g.,
$ python3 -m venv .venv

# Activate environment, e.g.,
$ . .venv/bin/activate

# Install dependencies:
$ pip install -r requirements.txt
```

## Launching

```bash
# Initialize redis
$ redis-server

# Initialize celery worker
$ celery -A app.make_celery.celery_app worker --loglevel=info

# Launch the app
$ python run.py
```
