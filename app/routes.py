from flask import render_template, request, Blueprint, jsonify
from app.utils import check_input_length
from app.tasks import async_correct_text

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def home():
    input_text = ""
    if request.method == "POST":
        input_text = request.form["text"]
        if not input_text:
            return jsonify({"error": "Please enter some text to correct."}), 400
        if not check_input_length(input_text):
            return jsonify({"error": "Input text exceeds length limit."}), 400

        task = async_correct_text.apply_async(args=[input_text])
        return jsonify({"task_id": task.id}), 202

    return render_template("index.html")


@bp.route("/task/<task_id>", methods=["GET"])
def get_task_result(task_id):
    task = async_correct_text.AsyncResult(task_id)
    if task.state == "PENDING":
        response = {"state": task.state, "status": "Processing..."}
    elif task.state == "SUCCESS":
        if "error" in task.result:  # Task failed due to an exception
            response = {"state": "FAILURE", "status": task.result["error"]}
        else:
            response = {"state": task.state, "result": task.result}
    else:
        response = {"state": "FAILURE", "status": "Error processing your request."}
    return jsonify(response)
