# OCR-Microservice
OCR Microservice Built in Flask

1. Create virtualenv with 'python3 -m venv env'.
2. Activate virtualenv with 'source env/bin/activate'.
3. Run 'pip install -r requirements.txt' to install dependencies. (Also need to install tesseract-ocr: https://github.com/tesseract-ocr/tesseract)
4. To start app in debug mode for development run 'python3 wsgi.py'.
5. To deploy app using gunicorn run 'gunicorn wsgi:handler'.

# Endpoint
This microservice has one endpoint:

POST /ocr 
  - Endpoint looks for a file in the key "file" in the request body

Example Response:
  {
    "text": "Mild Splendour of the various-vested Night!\nMother of wildly-working visions! hail!\nI watch thy gliding, while with watery light\nThy weak eye    
    glimmers through a fleecy veil;\nAnd when thou lovest thy pale orb to shroud\nBehind the gather’d blackness lost on high;\nAnd when thou dartest from the wind-
    rent cloud\nThy placid lightning o’er the awaken’d sky.\n"
  }

Error Response:
  {
    "Error": "Missing key with name of \"file\" in POST request"
  }


