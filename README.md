# OCR-Microservice
OCR Microservice Built in Flask

1. Create virtualenv with 'python3 -m venv env'.
2. Activate virtualenv with 'source env/bin/activate'.
3. Run 'pip install -r requirements.txt' to install dependencies. (Also need to install tesseract-ocr: https://github.com/tesseract-ocr/tesseract)
4. To start app in debug mode for development run 'python3 wsgi.py'.
5. To deploy app using gunicorn run 'gunicorn wsgi:handler'.
