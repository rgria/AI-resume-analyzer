from flask import Flask, render_template, request
from resume_parser import extract_text
from analyzer import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        resume = request.files["resume"]
        job_description = request.form["job"]

        resume_text = extract_text(resume)
        result = analyze_resume(resume_text, job_description)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
