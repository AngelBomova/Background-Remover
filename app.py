from pathlib import Path
from uuid import uuid4

from flask import Flask, abort, render_template, request, send_file
from rembg import remove
from werkzeug.utils import secure_filename


BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files.get("image")
        if not image or not image.filename:
            abort(400, "No image uploaded.")

        original_name = secure_filename(image.filename)
        extension = Path(original_name).suffix.lower()
        if extension not in ALLOWED_EXTENSIONS:
            abort(400, "Only PNG and JPG images are supported.")

        UPLOAD_DIR.mkdir(exist_ok=True)
        OUTPUT_DIR.mkdir(exist_ok=True)

        file_id = uuid4().hex
        upload_path = UPLOAD_DIR / f"{file_id}{extension}"
        output_path = OUTPUT_DIR / f"{Path(original_name).stem or file_id}-no-bg.png"

        image.save(upload_path)
        output_path.write_bytes(remove(upload_path.read_bytes()))

        return send_file(output_path, mimetype="image/png", as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    UPLOAD_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    app.run(debug=True)
