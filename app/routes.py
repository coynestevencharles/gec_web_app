from flask import render_template, request, Blueprint, flash, redirect, url_for
from app.models import correct_text, check_input_length

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def home():
    input_text = ""
    corrected_text = ""
    if request.method == "POST":
        input_text = request.form["text"]
        # Handle blank input
        if not input_text:
            flash("Please enter some text to correct.", "error")
            return redirect(url_for("main.home"))
        # Handle inputs that are too long
        elif not check_input_length(input_text):
            flash("Input text exceeds length limit. Please reduce the length and try again.", "error")
            return render_template("index.html", corrected_text=corrected_text, input_text=input_text)
        corrected_text = correct_text(input_text)
    return render_template("index.html", corrected_text=corrected_text, input_text=request.form.get('text', ''))
