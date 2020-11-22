from python:3.7-slim

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/app.py app.py
COPY ./app/model.pkl model.pkl
COPY ./app/scaler.pkl scaler.pkl

ENTRYPOINT ["python", "./app.py"]