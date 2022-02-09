# Code Reference: https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/

from flask import Flask, request, jsonify
import os
import tempfile
from werkzeug.utils import secure_filename
import cv2
import pytesseract

UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename) -> bool:
    """Checks if the filename has an allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def ocr(filepath) -> str:
    """Reads the image at the filepath and returns the OCR text"""
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(img, config=custom_config)


def create_app() -> Flask:
    """Assembles and returns application."""
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000  # set max size to 2MB

    @app.route('/ocr', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return jsonify({'Error': 'Missing key with name of "file" in POST request'}), 422

        file = request.files['file']

        if file.filename == '':
            return jsonify({'Error': 'No file selected'}), 422

        if not allowed_file(file.filename):
            return jsonify({'Error': 'File type not allowed'}), 422

        if file:
            try:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                ocr_text = ocr(filepath)
                return jsonify({'text': ocr_text}), 200
            except werkzeug.exceptions.RequestEntityTooLarge:
                return jsonify({'Error': 'File too large'}), 413

    return app
