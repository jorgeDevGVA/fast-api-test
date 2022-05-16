from werkzeug.utils import secure_filename
from PIL import Image
from fastapi import FastAPI, File, UploadFile
import uvicorn
import os
import pytesseract

UPLOAD_FOLDER = 'images'

app = FastAPI()

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    NO_VALID_IMAGE = 'No se ha proporcionado una imagen válida.'
    try:
        img = Image.open(file.file)
        text = pytesseract.image_to_string(img,'spa')
    except Exception as e:
        return NO_VALID_IMAGE
    return text

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
