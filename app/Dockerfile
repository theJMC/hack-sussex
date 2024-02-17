FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV FLASK_APP="__init__.py"

COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=1337"]
