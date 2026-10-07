from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

sys.path.insert(0, PROJECT_ROOT)

from routes.upload import upload_bp
from routes.summary import summary_bp
from routes.insights import insights_bp
from routes.terms import terms_bp
from routes.qa import qa_bp
from routes.gaps import gaps_bp

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.register_blueprint(upload_bp)
app.register_blueprint(summary_bp)
app.register_blueprint(insights_bp)
app.register_blueprint(terms_bp)
app.register_blueprint(qa_bp)
app.register_blueprint(gaps_bp)


@app.route("/")
def home():
    return {
        "success": True,
        "message": "Research Paper AI Backend is running"
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


@app.route("/test")
def test_page():
    return send_from_directory(".", "test_upload.html")
@app.route("/test-qa")
def test_qa_page():
    return send_from_directory(".", "test_qa.html")


if __name__ == "__main__":
    app.run(debug=True)