FROM python:3.10-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY app.py .
COPY recommender.py .
COPY training/ training/
COPY data/ data/

# Train model during build (Linux cloud build)
RUN python training/train_recommender.py

EXPOSE 5000

CMD ["python", "app.py"]


