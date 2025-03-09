FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
COPY Scores.txt /Scores.txt
CMD ["python", "MainScores.py"]