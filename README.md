# Grammatical Error Correction Web App

A simple web application that accepts input text and corrects it using a natural language processing model.

This is being built from the bottom up as an exercise in model training and deployment.

Planning to implement the following:

* An "error correction" tool that directly fixes input sentences.
* An "error checker" tool that highlights errors for the user's consideration.

Currently, a basic version of the corrector is available:

![Screenshot of the error correction tool](assets/error_correction_ui_screenshot.png?raw=true)

## Setup

Create an environment for this project, e.g.,
```
$ python3 -m venv .venv
```

Activate environment, e.g.,
```
$ . .venv/bin/activate
```

Install dependencies:
```
$ pip install -r requirements.txt
```

## Launching

```
$ python run.py
```