from pathlib import Path

from flask import Flask, render_template, request


BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Import remove from rembg here when wiring up the processing flow.
        # TODO: Save the uploaded image, remove the background, and return the new file.
        pass

    return render_template("index.html")


if __name__ == "__main__":
    UPLOAD_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    app.run(debug=True)
