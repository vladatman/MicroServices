FROM python:3.9-slim-buster
LABEL authors="Vladyslav Atamanchuk"

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY application.py ./

EXPOSE 7000

CMD [ "python", "application.py" ]
