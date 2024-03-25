from flask import render_template, request, Blueprint
from app.models import correct_text

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def home():
    corrected_text = ""
    if request.method == "POST":
        text = request.form["text"]
        corrected_text = correct_text(text)
    return render_template("index.html", corrected_text=corrected_text)
