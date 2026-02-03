FROM python:3.10-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install -r requirements.txt \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    --default-timeout=100 \
    -i https://pypi.org/simple

# Copy code
COPY app.py .
COPY recommender.py .
COPY training/ training/
COPY data/ data/

# Train model during build (Linux cloud build)
RUN python training/train_recommender.py

EXPOSE 5000

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]



