import joblib
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    """HTMLページをレンダリングします."""
    return render_template("index.html")


@app.route("/api/judge")
def api_judge():
    """手書き文字を判定します"""
    return "-1"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
