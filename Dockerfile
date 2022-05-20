FROM python:3

WORKDIR /usr/src/fastapi-test
EXPOSE 8000
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt install tesseract-ocr -y
RUN apt install tesseract-ocr-spa -y
COPY app2.py app2.py


CMD [ "python", "app2.py" ]