FROM python:3.11-slim
WORKDIR /app
COPY csv_exporter.py .
RUN pip install prometheus_client
CMD ["python", "csv_exporter.py"]